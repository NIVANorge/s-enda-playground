from dataclasses import dataclass, field
from typing import List, Optional
from bindings.gmd.length_type import LengthType
from bindings.gmd.line_string_segment_array_property_type import LineStringSegmentArrayPropertyType
from bindings.gmd.point_property import PointProperty
from bindings.gmd.pos import Pos
from bindings.gmd.pos_list import PosList
from bindings.gmd.triangulated_surface_type import TriangulatedSurfaceType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TinType(TriangulatedSurfaceType):
    stop_lines: List[LineStringSegmentArrayPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "stopLines",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    break_lines: List[LineStringSegmentArrayPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "breakLines",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    max_length: Optional[LengthType] = field(
        default=None,
        metadata={
            "name": "maxLength",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    control_point: Optional["TinType.ControlPoint"] = field(
        default=None,
        metadata={
            "name": "controlPoint",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )

    @dataclass
    class ControlPoint:
        pos_list: Optional[PosList] = field(
            default=None,
            metadata={
                "name": "posList",
                "type": "Element",
                "namespace": "http://www.opengis.net/gml",
            }
        )
        pos: List[Pos] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.opengis.net/gml",
            }
        )
        point_property: List[PointProperty] = field(
            default_factory=list,
            metadata={
                "name": "pointProperty",
                "type": "Element",
                "namespace": "http://www.opengis.net/gml",
            }
        )
