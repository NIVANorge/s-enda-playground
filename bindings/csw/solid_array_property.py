from dataclasses import dataclass
from bindings.csw.solid_array_property_type import SolidArrayPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class SolidArrayProperty(SolidArrayPropertyType):
    class Meta:
        name = "solidArrayProperty"
        namespace = "http://www.opengis.net/gml"
