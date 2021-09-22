from dataclasses import dataclass, field
from typing import List
from bindings.csw_publication.line_string_segment import LineStringSegment

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class LineStringSegmentArrayPropertyType:
    line_string_segment: List[LineStringSegment] = field(
        default_factory=list,
        metadata={
            "name": "LineStringSegment",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
