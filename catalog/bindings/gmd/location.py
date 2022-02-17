from dataclasses import dataclass
from bindings.gmd.location_property_type import LocationPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Location(LocationPropertyType):
    class Meta:
        name = "location"
        namespace = "http://www.opengis.net/gml"
