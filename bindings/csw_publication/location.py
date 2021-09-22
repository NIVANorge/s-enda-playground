from dataclasses import dataclass
from bindings.csw_publication.location_property_type import LocationPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Location(LocationPropertyType):
    """
    Deprecated in GML 3.1.0.
    """
    class Meta:
        name = "location"
        namespace = "http://www.opengis.net/gml"
