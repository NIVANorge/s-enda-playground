from dataclasses import dataclass
from bindings.wfs.property_type import PropertyType

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class Property(PropertyType):
    class Meta:
        namespace = "http://www.opengis.net/wfs/2.0"
