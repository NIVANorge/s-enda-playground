#%%
from bindings.csw.get_capabilities_2 import GetCapabilities2
from owslib.csw import CatalogueServiceWeb
from owslib.catalogue.csw2 import CswRecord
from lxml import etree
import requests
from xsdata.formats.dataclass.serializers import config

# %%
def pretty_print(xml_bytes):
    """
    Pretty print XML bytes.
    """
    root = etree.XML(xml_bytes)
    print(etree.tostring(root, pretty_print=True).decode())


# %%
CSW_HOST = "http://sjoa.niva.no/geonetwork/srv/eng/csw"

csw = CatalogueServiceWeb(CSW_HOST)
#%%
csw.getrecords2(esn="full", maxrecords=1000)
parsed_records = csw.records.values()
record = list(parsed_records)[0]
#%%
pretty_print(record.xml)
# %%
record.identifier
# %%

MET_HOST = "https://csw.s-enda.k8s.met.no"
# %%
met_csw = CatalogueServiceWeb(MET_HOST)
# %%
met_records = met_csw.getrecords2()
# %%
check_txt = requests.post(
    "https://csw.s-enda.k8s.met.no", data=open("test_query.xml").read()
).text
# %%
# http://schemas.opengis.net/csw/2.0.2/CSW-discovery.xsd
# %%
from bindings.csw import (
    GetRecords,
    Query,
    Constraint,
    Filter,
    Intersects,
    Polygon,
    Exterior,
    LinearRing,
    PosList,
    GetRecordsResponse,
    Transaction,
    Record,
    References,
    GetDomain,
    GetCapabilities2,
    AcceptVersionsType
)
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
get_records = GetRecords(
    result_type="results",
    query=Query(
        type_names=["csw:Record"],
        element_set_name="full",
        constraint=Constraint(
            version="1.1.0",
            filter=Filter(
                intersects=Intersects(
                    property_name="ows:BoundingBox",
                    polygon=Polygon(
                        exterior=Exterior(
                            linear_ring=LinearRing(pos_list=PosList(value=pos_values))
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
records = parser.from_string(resp.text, GetRecordsResponse)

# %%
records.search_results.record[0]
# %%
check_rec = parser.from_string(check_txt, GetRecordsResponse)
# %%
check_rec.search_results.record[0].references[1].content
# %%
transaction = Transaction(insert=Record(references=References()))
# %%
transaction.version
# %%
requests.post(
    MET_HOST, serializer.render(GetDomain(parameter_name="GetRecords.resultType"))
).text
# %%
cap = GetCapabilities2(
    service="CSW", accept_versions=AcceptVersionsType(version=["2.0.0"])
)
#%%
requests.post(MET_HOST, serializer.render(cap)).text

# %%

get_records_small = GetRecords(
    result_type="results",
    query=Query(
        type_names=["csw:Record"],
        element_set_name="full"
    ),
)

# %%
#http://sjoa.niva.no/geonetwork/srv/eng/csw?SERVICE=CSW&VERSION=2.0.2&REQUEST=GetCapabilities
CSW_HOST = "http://sjoa.niva.no/geonetwork/srv/eng/csw?SERVICE=CSW&VERSION=2.0.2"

requests.post(CSW_HOST, serializer.render(get_records_small, ns_map={"csw": "http://www.opengis.net/cat/csw/2.0.2"})).text
# %%
