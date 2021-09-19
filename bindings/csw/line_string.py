from dataclasses import dataclass
from bindings.csw.line_string_type import LineStringType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class LineString(LineStringType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
