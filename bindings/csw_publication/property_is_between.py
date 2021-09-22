from dataclasses import dataclass
from bindings.csw_publication.property_is_between_type import PropertyIsBetweenType

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class PropertyIsBetween(PropertyIsBetweenType):
    class Meta:
        namespace = "http://www.opengis.net/ogc"
