from dataclasses import dataclass
from bindings.gmd.prime_meridian_property_type import PrimeMeridianPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class UsesPrimeMeridian(PrimeMeridianPropertyType):
    class Meta:
        name = "usesPrimeMeridian"
        namespace = "http://www.opengis.net/gml"
