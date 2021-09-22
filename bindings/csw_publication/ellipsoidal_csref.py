from dataclasses import dataclass
from bindings.csw_publication.ellipsoidal_csref_type import EllipsoidalCsrefType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class EllipsoidalCsref(EllipsoidalCsrefType):
    class Meta:
        name = "ellipsoidalCSRef"
        namespace = "http://www.opengis.net/gml"
