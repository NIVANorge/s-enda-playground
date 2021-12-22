[![fair-software.eu](https://img.shields.io/badge/fair--software.eu-%E2%97%8F%20%20%E2%97%8B%20%20%E2%97%8B%20%20%E2%97%8B%20%20%E2%97%8B-red)](https://fair-software.eu)

Playground
==========

A bunch of scripts to play with new and old standards for geospatial data. Some other CF resources can be found at [cf-python](https://github.com/NCAS-CMS/cf-training) or the at [xarray](https://xarray.pydata.org/en/stable/user-guide/io.html)

Generate
========

Using the fairly new xsdata to generate bindings, a better alternative than pyxb.

```bash
xsdata http://schemas.opengis.net/csw/2.0.2/CSW-discovery.xsd --package bindings.csw --config xsdata.xml
xsdata https://www.isotc211.org/2005/gmd/gmd.xsd --package bindings.gmd --config xsdata.xml
xsdata http://schemas.opengis.net/ows/2.0/owsAll.xsd --package bindings.ows --config xsdata.xml
xsdata http://schemas.opengis.net/wfs/2.0/wfs.xsd --package bindings.wfs --config xsdata.xml
```

Units
=====

```bash
sudo apt-get install libudunits2-dev
```