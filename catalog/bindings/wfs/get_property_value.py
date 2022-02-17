from dataclasses import dataclass
from bindings.wfs.get_property_value_type import GetPropertyValueType

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class GetPropertyValue(GetPropertyValueType):
    class Meta:
        namespace = "http://www.opengis.net/wfs/2.0"
