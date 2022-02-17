Generate
========

Many of the older ogc standards comes with xml schemas, that means one can, for example, use xsdata to generate data model bindings. Not saying that is something you should do, as there already exists libraries for many of these standards;)

```bash
xsdata http://schemas.opengis.net/csw/2.0.2/CSW-discovery.xsd --package bindings.csw --config xsdata.xml
xsdata https://www.isotc211.org/2005/gmd/gmd.xsd --package bindings.gmd --config xsdata.xml
xsdata http://schemas.opengis.net/ows/2.0/owsAll.xsd --package bindings.ows --config xsdata.xml
xsdata http://schemas.opengis.net/wfs/2.0/wfs.xsd --package bindings.wfs --config xsdata.xml
```
