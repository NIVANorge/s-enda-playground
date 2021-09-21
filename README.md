xsdata http://schemas.opengis.net/csw/2.0.2/CSW-discovery.xsd --config xsdata.xml

```bash
docker run --name pycsw-test --publish 8000:8000 geopython/pycsw
```