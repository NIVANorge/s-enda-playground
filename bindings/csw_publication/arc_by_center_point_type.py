from dataclasses import dataclass, field
from typing import Optional
from bindings.csw_publication.abstract_curve_segment_type import AbstractCurveSegmentType
from bindings.csw_publication.angle_type import AngleType
from bindings.csw_publication.coordinates import Coordinates
from bindings.csw_publication.curve_interpolation_type import CurveInterpolationType
from bindings.csw_publication.length_type import LengthType
from bindings.csw_publication.point_property import PointProperty
from bindings.csw_publication.point_rep import PointRep
from bindings.csw_publication.pos import Pos
from bindings.csw_publication.pos_list import PosList

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ArcByCenterPointType(AbstractCurveSegmentType):
    """This variant of the arc requires that the points on the arc have to be
    computed instead of storing the coordinates directly.

    The control point is the center point of the arc plus the radius and
    the bearing at start and end. This represenation can be used only in
    2D.

    :ivar pos:
    :ivar point_property:
    :ivar point_rep: Deprecated with GML version 3.1.0. Use
        "pointProperty" instead. Included for backwards compatibility
        with GML 3.0.0.
    :ivar pos_list:
    :ivar coordinates: Deprecated with GML version 3.1.0. Use "posList"
        instead.
    :ivar radius: The radius of the arc.
    :ivar start_angle: The bearing of the arc at the start.
    :ivar end_angle: The bearing of the arc at the end.
    :ivar interpolation: The attribute "interpolation" specifies the
        curve interpolation mechanism used for this segment. This
        mechanism uses the control points and control parameters to
        determine the position of this curve segment. For an
        ArcByCenterPoint the interpolation is fixed as
        "circularArcCenterPointWithRadius".
    :ivar num_arc: Since this type describes always a single arc, the
        attribute is fixed to "1".
    """
    pos: Optional[Pos] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    point_property: Optional[PointProperty] = field(
        default=None,
        metadata={
            "name": "pointProperty",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    point_rep: Optional[PointRep] = field(
        default=None,
        metadata={
            "name": "pointRep",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
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
    radius: Optional[LengthType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    start_angle: Optional[AngleType] = field(
        default=None,
        metadata={
            "name": "startAngle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    end_angle: Optional[AngleType] = field(
        default=None,
        metadata={
            "name": "endAngle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    interpolation: CurveInterpolationType = field(
        init=False,
        default=CurveInterpolationType.CIRCULAR_ARC_CENTER_POINT_WITH_RADIUS,
        metadata={
            "type": "Attribute",
        }
    )
    num_arc: int = field(
        init=False,
        default=1,
        metadata={
            "name": "numArc",
            "type": "Attribute",
            "required": True,
        }
    )
