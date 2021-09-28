from dataclasses import dataclass
from bindings.wfs.property_is_null_type import PropertyIsNullType

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class PropertyIsNull(PropertyIsNullType):
    class Meta:
        namespace = "http://www.opengis.net/fes/2.0"
