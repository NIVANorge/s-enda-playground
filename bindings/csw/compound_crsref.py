from dataclasses import dataclass
from bindings.csw.compound_crsref_type import CompoundCrsrefType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CompoundCrsref(CompoundCrsrefType):
    class Meta:
        name = "compoundCRSRef"
        namespace = "http://www.opengis.net/gml"
