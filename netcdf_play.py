#%%
import os
from datetime import datetime

import requests
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from bindings import csw, gmd
from bindings.csw.feature_array_property_type import File

from owslib.catalogue import csw2
from owslib import fes2
# %%
MET_HOST = "https://csw.s-enda.k8s.met.no"
# %%
serializer = XmlSerializer(config=SerializerConfig(pretty_print=True))
parser = XmlParser(config=ParserConfig())
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
                    property_name=csw.PropertyName(["dc:subject"]),
                    literal=csw.Literal(["*Net*"]),
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
resp.text
# %%
