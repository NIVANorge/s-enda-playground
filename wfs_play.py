#%%
import os
from datetime import datetime

import requests
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from bindings import wfs
# %%
MILJO_HOST = "https://kart.miljodirektoratet.no/geoserver/forvaltningsplaner_havomrader/wfs"

# %%
serializer = XmlSerializer(config=SerializerConfig(pretty_print=True))
parser = XmlParser(config=ParserConfig())
ns_map = {"wfs": "http://www.opengis.net/wfs"}
# %%
q_features = wfs.GetFeature(query=[wfs.Query(type_names=["forvaltningsplaner_havomrader_omrade"])])
#%%
resp = requests.post(
    MILJO_HOST,
    serializer.render(q_features, ns_map=ns_map),
)
#%%
feature_collection = parser.from_string(resp.text, wfs.FeatureCollection)
# %%
feature_collection.number_returned
# %%

for m in feature_collection.member:
    print(m)
# %%
feature_collection.member[1].content[0].children[0].text
# %%
feature_collection.member[1].content[0].children[3].children[0]
# %%
