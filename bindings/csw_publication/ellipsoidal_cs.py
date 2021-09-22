from dataclasses import dataclass
from bindings.csw_publication.ellipsoidal_cstype import EllipsoidalCstype

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class EllipsoidalCs(EllipsoidalCstype):
    class Meta:
        name = "EllipsoidalCS"
        namespace = "http://www.opengis.net/gml"
