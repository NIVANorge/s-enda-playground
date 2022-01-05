[![fair-software.eu](https://img.shields.io/badge/fair--software.eu-%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8B%20%20%E2%97%8B%20%20%E2%97%8B-orange)](https://fair-software.eu)

Playground
==========

A bunch of scripts to play with technologies relevant for s-enda

* [collection](./collections) folder a set of [Postman collections](https://www.postman.com/collection/). These can be used to interact with csw services.
* [hello-xarray](./hello-xarray) some samples to work with [xarray](https://xarray.pydata.org/en/stable/user-guide/io.html) and trying to follow [cf-convention](https://cfconventions.org/)
* [catalog](./catalog) some sample scripts to play with ogc(mostly csw) and xsdata

Install
-------

```bash
poetry install
```

it can be practical to use `poetry config virtualenvs.in-project true`.