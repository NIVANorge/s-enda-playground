from dataclasses import dataclass
from bindings.gmd.ellipsoidal_csproperty_type import EllipsoidalCspropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class EllipsoidalCsref(EllipsoidalCspropertyType):
    class Meta:
        name = "ellipsoidalCSRef"
        namespace = "http://www.opengis.net/gml"
