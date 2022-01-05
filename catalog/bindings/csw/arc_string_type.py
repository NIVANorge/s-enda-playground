from dataclasses import dataclass, field
from typing import List, Optional
from bindings.csw.abstract_curve_segment_type import AbstractCurveSegmentType
from bindings.csw.coordinates import Coordinates
from bindings.csw.curve_interpolation_type import CurveInterpolationType
from bindings.csw.point_property import PointProperty
from bindings.csw.point_rep import PointRep
from bindings.csw.pos import Pos
from bindings.csw.pos_list import PosList

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ArcStringType(AbstractCurveSegmentType):
    """
    An ArcString is a curve segment that uses three-point circular arc
    interpolation.

    :ivar pos:
    :ivar point_property:
    :ivar point_rep: Deprecated with GML version 3.1.0. Use
        "pointProperty" instead. Included for backwards compatibility
        with GML 3.0.0.
    :ivar pos_list:
    :ivar coordinates: Deprecated with GML version 3.1.0. Use "posList"
        instead.
    :ivar interpolation: The attribute "interpolation" specifies the
        curve interpolation mechanism used for this segment. This
        mechanism uses the control points and control parameters to
        determine the position of this curve segment. For an ArcString
        the interpolation is fixed as "circularArc3Points".
    :ivar num_arc: The number of arcs in the arc string can be
        explicitly stated in this attribute. The number of control
        points in the arc string must be 2 * numArc + 1.
    """
    pos: List[Pos] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 3,
            "sequential": True,
        }
    )
    point_property: List[PointProperty] = field(
        default_factory=list,
        metadata={
            "name": "pointProperty",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 3,
            "sequential": True,
        }
    )
    point_rep: List[PointRep] = field(
        default_factory=list,
        metadata={
            "name": "pointRep",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 3,
            "sequential": True,
        }
    )
    pos_list: Optional[PosList] = field(
        default=None,
        metadata={
            "name": "posList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    coordinates: Optional[Coordinates] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    interpolation: CurveInterpolationType = field(
        init=False,
        default=CurveInterpolationType.CIRCULAR_ARC3_POINTS,
        metadata={
            "type": "Attribute",
        }
    )
    num_arc: Optional[int] = field(
        default=None,
        metadata={
            "name": "numArc",
            "type": "Attribute",
        }
    )
