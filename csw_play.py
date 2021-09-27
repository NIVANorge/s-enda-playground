#%%
from bindings.csw.feature_array_property_type import File
from bindings import csw, gmd
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.models.generics import AnyElement
import requests

# %%
MET_HOST = "https://csw.s-enda.k8s.met.no"
PYCSW_HOST = "http://localhost:8000"
GEONORGE_BETA_HOST = "https://www.geonorge.no/geonetworkbeta/srv/nor/csw"
GEONORGE_HOST = "https://www.geonorge.no/geonetwork/srv/nor/csw"
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
q_records = csw.GetRecords(
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
                            linear_ring=csw.LinearRing(
                                pos_list=csw.PosList(value=pos_values)
                            )
                        )
                    ),
                )
            ),
        ),
    ),
)
# %%
serializer = XmlSerializer(config=SerializerConfig(pretty_print=True))
ns_map = {"csw": "http://www.opengis.net/cat/csw/2.0.2"}
# %%
resp = requests.post(
    MET_HOST,
    serializer.render(q_records, ns_map=ns_map),
)
# %%
parser = XmlParser(config=ParserConfig())
# %%
records = parser.from_string(resp.text, csw.GetRecordsResponse)
# %%
records.search_results.record[0]
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
q_records_title = csw.GetRecords(
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
                    property_name=csw.PropertyName(["dc:title"]),
                    literal=csw.Literal(["*Iddefjorden*"]),
                )
            ),
        ),
    ),
)

# %%
# http://sjoa.niva.no/geonetwork/srv/eng/csw?SERVICE=CSW&VERSION=2.0.2&REQUEST=GetCapabilities
CSW_HOST = "http://sjoa.niva.no/geonetwork/srv/eng/csw"

resp = requests.post(
    CSW_HOST,
    headers={"Content-Type": "application/xml"},
    data=serializer.render(
        q_records_title, ns_map={"csw": "http://www.opengis.net/cat/csw/2.0.2"}
    ),
)
# %%
transaction = csw.Transaction(
    insert=[
        csw.InsertType(
            other_element=[
                csw.Record(
                    identifier=["mock.1234567"],
                    title=[csw.Title3("Iddefjorden_hydrografi")],
                    abstract=[csw.Abstract2("My Long abstract")],
                    references=[
                        csw.References(
                            content=[
                                "http://aquamonitor.niva.no/nmdc/archives/jmgwuvw/Iddefjorden_hydrografi.nc"
                            ]
                        )
                    ],
                ),
            ],
            type_name=["csw:Record"],
        )
    ]
)

# %%
resp = requests.post(
    PYCSW_HOST,
    headers={"Content-Type": "application/xml"},
    data=serializer.render(
        transaction, ns_map={"csw": "http://www.opengis.net/cat/csw/2.0.2"}
    ),
)
# %%
resp.text

# %%
resp = requests.post(
    GEONORGE_BETA_HOST, serializer.render(cap), auth=("admin", "admin")
).text
# %%
resp
# %%
with open("xml/gmd_sample.xml", "rb") as f:
    gmd_metadata = parser.from_bytes(f.read(), csw.MetaData2)
# %%
gmd_metadata
# %%
transaction_gmd = csw.Transaction(
    insert=[
        csw.InsertType(
            other_element=[gmd_metadata],
            type_name=["csw:Record"],
        )
    ]
)
#%%
gmd.MdMetadata()
#%%
transaction_gmd = csw.Transaction(
    insert=[
        csw.InsertType(
            other_element=[],
            type_name=["csw:Record"],
        )
    ]
)

# %%
serializer.render(
    transaction_gmd, ns_map={"csw": "http://www.opengis.net/cat/csw/2.0.2"}
)
# %%

gmd.content[3]
# %%
