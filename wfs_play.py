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
from bindings import wfs, gmd

# %%
MILJO_HOST = (
    "https://kart.miljodirektoratet.no/geoserver/forvaltningsplaner_havomrader/wfs"
)

# %%
serializer = XmlSerializer(config=SerializerConfig(pretty_print=True))
parser = XmlParser(config=ParserConfig())
ns_map = {"wfs": "http://www.opengis.net/wfs", "gml": "http://www.opengis.net/gml"}
# %%
# can also be json
q_features = wfs.GetFeature(
    query=[
        wfs.Query(
            type_names=["forvaltningsplaner_havomrader_omrade"],
            srs_name="EPSG:4326",
            filter=wfs.Filter(
                resource_id=[
                    wfs.ResourceId(rid="forvaltningsplaner_havomrader_omrade.1")
                ]
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
#json.loads(resp.text)
#%%
feature_collection = parser.from_string(resp.text, wfs.FeatureCollection)
# %%
feature_collection.member[0]
# %%
feature_collection

# %%

for m in feature_collection.member:
    print(m.content[0].children[0].text)
# %%
feature_collection.member[0].content[0].children[0].text
# %%
feature_collection.member[0].content[0].children[3].children[0]
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
    outputFormat="json"
)
#%%
world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
world.crs
#%%

regions = geopandas.read_file(bytes_stream)
regions.crs
#%%
fig, ax = plt.subplots(figsize=(15, 15))
world.plot(ax=ax, alpha=0.7, color="pink")
regions.plot(ax=ax)
# %%
