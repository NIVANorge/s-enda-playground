from dataclasses import dataclass
from bindings.csw_publication.property_is_null_type import PropertyIsNullType

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class PropertyIsNull(PropertyIsNullType):
    class Meta:
        namespace = "http://www.opengis.net/ogc"
