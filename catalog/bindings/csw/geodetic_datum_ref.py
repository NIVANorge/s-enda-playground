from dataclasses import dataclass
from bindings.csw.geodetic_datum_ref_type import GeodeticDatumRefType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GeodeticDatumRef(GeodeticDatumRefType):
    class Meta:
        name = "geodeticDatumRef"
        namespace = "http://www.opengis.net/gml"
