from dataclasses import dataclass
from bindings.csw_publication.derived_crstype_type import DerivedCrstypeType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DerivedCrstype(DerivedCrstypeType):
    class Meta:
        name = "derivedCRSType"
        namespace = "http://www.opengis.net/gml"
