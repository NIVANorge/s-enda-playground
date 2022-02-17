from dataclasses import dataclass
from bindings.csw.derived_crsref_type import DerivedCrsrefType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DerivedCrsref(DerivedCrsrefType):
    class Meta:
        name = "derivedCRSRef"
        namespace = "http://www.opengis.net/gml"
