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
from generated import record

# %%
