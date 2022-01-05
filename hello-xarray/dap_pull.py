#%%
from datetime import datetime

import requests
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from catalog.bindings import csw
from catalog.bindings.csw.feature_array_property_type import File

from netCDF4 import Dataset
# %%
MET_HOST = "https://csw.s-enda.k8s.met.no"
GEONORGE_HOST = "https://www.geonorge.no/geonetwork/srv/nor/csw"
# %%
serializer = XmlSerializer(config=SerializerConfig(pretty_print=True))
parser = XmlParser(config=ParserConfig())
sloppy_parser = XmlParser(config=ParserConfig(fail_on_unknown_properties=False))
ns_map = {"csw": "http://www.opengis.net/cat/csw/2.0.2", "dct":"http://purl.org/dc/terms/"}
# %%
q_records = csw.GetRecords(
    result_type="results",
    query=csw.Query(
        type_names=["csw:Record"],
        element_set_name="full",
        constraint=csw.Constraint(
            version="1.1.0",
            filter=csw.Filter(
                property_is_like=csw.PropertyIsLike(
                    wild_card="*",
                    single_char="?",
                    escape_char="\\",
                    match_case="false",
                    property_name=csw.PropertyName(["csw:AnyText"]),
                    literal=csw.Literal(["*OPENDAP*"]),
                )
            ),
        ),
    ),
)

#%%
resp = requests.post(
    MET_HOST,
    headers={"Content-Type": "application/xml"},
    data=serializer.render(
        q_records, ns_map={"csw": "http://www.opengis.net/cat/csw/2.0.2"}
    ),
)
# %%
records = parser.from_string(resp.text, csw.GetRecordsResponse)
# %%
records.search_results.number_of_records_matched
# %%
open_dap_references = [r for r in records.search_results.record[0].references if r.scheme=="OPENDAP:OPENDAP"]
# %%
data_set = Dataset(open_dap_references[0].content[0])
# %%
for attr in data_set.ncattrs():
    if "vocab" in attr:
        print(f"{attr} = {data_set.getncattr(attr)}")
# %%
data_set.variables


# %%
