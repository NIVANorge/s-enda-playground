#%%
import os
from datetime import datetime

import requests
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from owslib.wfs import WebFeatureService
import geopandas
import json
import matplotlib.pyplot as plt
from bindings import wfs, csw
from lxml import etree

# See http://docs.opengeospatial.org/is/09-026r2/09-026r2.html#37
# %%
MILJO_HOST = (
    "https://kart.miljodirektoratet.no/geoserver/forvaltningsplaner_havomrader/wfs"
)
MET_HOST = "https://csw.s-enda.k8s.met.no"
GEONORGE_HOST = "https://www.geonorge.no/geonetwork/srv/nor/csw"
# %%
serializer = XmlSerializer(config=SerializerConfig(pretty_print=True))
parser = XmlParser(config=ParserConfig())
ns_map = {
    "wfs": "http://www.opengis.net/wfs",
    "csw": "http://www.opengis.net/cat/csw/2.0.2",
}
# %%
# can also be json
q_features = wfs.GetFeature(
    output_format="gml3",
    query=[
        wfs.Query(
            type_names=["forvaltningsplaner_havomrader_omrade"],
            srs_name="EPSG:4326",
            filter=wfs.Filter(
                property_is_like=wfs.PropertyIsLike(
                    wild_card="*",
                    single_char="?",
                    escape_char="\\",
                    match_case="false",
                    value_reference=wfs.ValueReference(value="navn_no"),
                    literal=wfs.Literal(content=["*Barents*"]),
                )
            ),
        )
    ],
)
#%%
resp = requests.post(
    MILJO_HOST,
    serializer.render(q_features, ns_map=ns_map),
)
#%%
feature_collection = etree.XML(resp.content)
#%%
polygon_node = feature_collection.xpath('//*[local-name()="Polygon"]')[0]
#%%
csw_polygon = parser.from_bytes(etree.tostring(polygon_node), csw.Polygon)
# %%
q_records = csw.GetRecords(
    result_type="results",
    max_records=35,
    query=csw.Query(
        type_names=["csw:Record"],
        element_set_name="full",
        constraint=csw.Constraint(
            version="1.1.0",
            filter=csw.Filter(
                intersects=csw.Intersects(
                    property_name=["ows:BoundingBox"], polygon=csw_polygon
                )
            ),
        ),
    ),
)
#%%
resp = requests.post(
    GEONORGE_HOST,
    headers={"Content-Type": "application/xml"},
    data=serializer.render(
        q_records, ns_map={"csw": "http://www.opengis.net/cat/csw/2.0.2"}
    ),
)
#%%
records = parser.from_string(resp.text, csw.GetRecordsResponse)
#%%
records.search_results.number_of_records_returned
#%%
for rec in records.search_results.record:
    print(rec.title)
    print(rec.abstract)
    print("")
#%%
wfs_client = WebFeatureService(MILJO_HOST)
#%%
wfs_client.contents[
    "forvaltningsplaner_havomrader:forvaltningsplaner_havomrader_omrade"
].boundingBoxWGS84
wfs_client.contents.keys()
#%%
bytes_stream = wfs_client.getfeature(
    typename=["forvaltningsplaner_havomrader:forvaltningsplaner_havomrader_omrade"],
    srsname="EPSG:4326",
    outputFormat="json",
)
#%%
world = geopandas.read_file(geopandas.datasets.get_path("naturalearth_lowres"))
world.crs
#%%

regions = geopandas.read_file(bytes_stream)
regions.crs
#%%
fig, ax = plt.subplots(figsize=(15, 15))
world.plot(ax=ax, alpha=0.7, color="pink")
regions.plot(ax=ax)
#%%
q_property = wfs.GetPropertyValue(
    value_reference="geom",
    query=wfs.Query(
        type_names=["forvaltningsplaner_havomrader_omrade"],
        srs_name="EPSG:4326",
        filter=wfs.Filter(
            property_is_like=wfs.PropertyIsLike(
                wild_card="*",
                single_char="?",
                escape_char="\\",
                match_case="false",
                value_reference=wfs.ValueReference(value="navn_no"),
                literal=wfs.Literal(content=["*Barents*"]),
            )
        ),
    ),
)
#%%
resp = requests.post(
    MILJO_HOST,
    serializer.render(q_property, ns_map=ns_map),
)
#%%
value_collection = parser.from_string(resp.text, wfs.ValueCollection)
#%%
with open("xml/barents.xml", "w") as f:
    serializer.write(
        f, value_collection.member[0].content[0].children[0], ns_map=ns_map
    )
