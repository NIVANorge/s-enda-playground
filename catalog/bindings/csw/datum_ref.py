from dataclasses import dataclass
from bindings.csw.datum_ref_type import DatumRefType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DatumRef(DatumRefType):
    class Meta:
        name = "datumRef"
        namespace = "http://www.opengis.net/gml"
