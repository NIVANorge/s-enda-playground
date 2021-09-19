from dataclasses import dataclass
from bindings.csw.property_name_type import PropertyNameType

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class PropertyName(PropertyNameType):
    class Meta:
        namespace = "http://www.opengis.net/ogc"
