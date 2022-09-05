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

Thredds
------

``` bash
https://thredds.t.niva.no/thredds/ncss/point/datasets/timeseries.nc?var=conductivity&var=salinity&north=59.951&west=10.750&east=10.751&south=59.950&time_start=1999-10-01T00:00:00Z&time_end=1999-10-05T00:00:00Z&timeStride=1&accept=csv
```