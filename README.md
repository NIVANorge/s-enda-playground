[![fair-software.eu](https://img.shields.io/badge/fair--software.eu-%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8B%20%20%E2%97%8B%20%20%E2%97%8B-orange)](https://fair-software.eu)

Playground
==========

A bunch of scripts to play with technologies relevant for s-enda

* [catalog](./catalog) some sample scripts to play with ogc(mostly csw) and xsdata
* [collection](./collections) a set of [Postman collections](https://www.postman.com/collection/) to interact with csw services.
* [hello-xarray](./hello-xarray) some samples to work with [xarray](https://xarray.pydata.org/en/stable/user-guide/io.html) and trying to follow [cf-convention](https://cfconventions.org/)

Install
-------

```bash
poetry install
```

it can be practical to use `poetry config virtualenvs.in-project true`.

ERDDAP
------

``` bash
http://localhost:8080/erddap/tabledap/datasets_bfaf_84b3_3aa5.htmlTable?time,longitude,latitude,sea_water_temperature
```