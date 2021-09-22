from dataclasses import dataclass
from bindings.csw_publication.line_string_segment_type import LineStringSegmentType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class LineStringSegment(LineStringSegmentType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
