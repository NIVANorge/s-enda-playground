#%%
from bindings import csw
from lxml.etree import QName
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
import requests

# %%
MET_HOST = "https://csw.s-enda.k8s.met.no"
# %%
pos_values = [
    47.00,
    -5.00,
    55.00,
    -5.00,
    55.00,
    20.00,
    47.00,
    20.00,
    47.00,
    -5.00,
]
get_records = csw.GetRecords(
    result_type="results",
    query=csw.Query(
        type_names=["csw:Record"],
        element_set_name="full",
        constraint=csw.Constraint(
            version="1.1.0",
            filter=csw.Filter(
                intersects=csw.Intersects(
                    property_name="ows:BoundingBox",
                    polygon=csw.Polygon(
                        exterior=csw.Exterior(
                            linear_ring=csw.LinearRing(pos_list=csw.PosList(value=pos_values))
                        )
                    ),
                )
            ),
        ),
    ),
)
# %%
serializer = XmlSerializer(config=SerializerConfig(pretty_print=True))
# %%
resp = requests.post(
    MET_HOST,
    serializer.render(
        get_records, ns_map={"csw": "http://www.opengis.net/cat/csw/2.0.2"}
    ),
)
# %%
config = ParserConfig(fail_on_unknown_properties=True)
parser = XmlParser(config=config)
# %%
records = parser.from_string(resp.text, csw.GetRecordsResponse)

# %%
records.search_results.record[0]
# %%
# %%
transaction = csw.Transaction(insert=csw.Record(references=csw.References()))
# %%
transaction.version
# %%
requests.post(
    MET_HOST, serializer.render(csw.GetDomain(parameter_name="GetRecords.resultType"))
).text
# %%
cap = csw.GetCapabilities2(
    service="CSW", accept_versions=csw.AcceptVersionsType(version=["2.0.0"])
)
#%%
requests.post(MET_HOST, serializer.render(cap)).text

# %%
get_records_small = csw.GetRecords(
    result_type="results",
    query=csw.Query(
        type_names=["csw:Record"],
        element_set_name="full"
    ),
)

# %%
#http://sjoa.niva.no/geonetwork/srv/eng/csw?SERVICE=CSW&VERSION=2.0.2&REQUEST=GetCapabilities
CSW_HOST = "http://sjoa.niva.no/geonetwork/srv/eng/csw?SERVICE=CSW&VERSION=2.0.2"

requests.post(CSW_HOST, serializer.render(get_records_small, ns_map={"csw": "http://www.opengis.net/cat/csw/2.0.2"})).text
# %%
csw.Subject2