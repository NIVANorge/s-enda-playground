#%%
from owslib.csw import CatalogueServiceWeb
from owslib.catalogue.csw2 import CswRecord
from lxml import etree
import requests
# %%
def pretty_print(xml_bytes):
    """
    Pretty print XML bytes.
    """
    root = etree.XML(xml_bytes)
    print(etree.tostring(root, pretty_print=True).decode())
# %%
CSW_HOST='http://sjoa.niva.no/geonetwork/srv/eng/csw'

csw = CatalogueServiceWeb(CSW_HOST)
#%%
csw.getrecords2(esn='full', maxrecords=1000)
parsed_records = csw.records.values()
record = list(parsed_records)[0]
#%%
pretty_print(record.xml)
# %%
record.identifier
# %%

MET_HOST = 'https://csw.s-enda.k8s.met.no'
# %%
met_csw = CatalogueServiceWeb(MET_HOST)
# %%
met_records = met_csw.getrecords2()
# %%
requests.post('https://csw.s-enda.k8s.met.no', data=open('test_query.xml').read()).text
# %%
#http://schemas.opengis.net/csw/2.0.2/CSW-discovery.xsd
# %%
from bindings.csw import GetRecords, Query, Constraint
from xsdata.formats.dataclass.serializers import XmlSerializer
import requests
# %%
get_records = GetRecords()
# %%
constraint = Constraint()
# %%
q = Query(element_set_name='full')
# %%
q
# %%
serializer = XmlSerializer()
# %%
serializer.render(get_records)
# %%
requests.post(MET_HOST, serializer.render(get_records))
# %%
