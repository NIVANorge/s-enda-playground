from dataclasses import dataclass
from bindings.csw_publication.abstract_time_primitive_type import TimePrimitivePropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ValidTime(TimePrimitivePropertyType):
    class Meta:
        name = "validTime"
        namespace = "http://www.opengis.net/gml"
