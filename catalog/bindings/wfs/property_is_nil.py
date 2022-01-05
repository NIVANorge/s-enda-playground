from dataclasses import dataclass
from bindings.wfs.property_is_nil_type import PropertyIsNilType

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class PropertyIsNil(PropertyIsNilType):
    class Meta:
        namespace = "http://www.opengis.net/fes/2.0"
