from dataclasses import dataclass, field
from typing import List, Optional
from bindings.csw.abstract_curve_segment_type import AbstractCurveSegmentType
from bindings.csw.curve_interpolation_type import CurveInterpolationType
from bindings.csw.point_property import PointProperty
from bindings.csw.pos import Pos
from bindings.csw.pos_list import PosList

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GeodesicStringType(AbstractCurveSegmentType):
    """A GeodesicString consists of sequence of geodesic segments.

    The type essentially combines a sequence of Geodesic into a single
    object. The GeodesicString is computed from two or more positions
    and an interpolation using geodesics defined from the geoid (or
    ellipsoid) of the co-ordinate reference system being used.

    :ivar pos_list:
    :ivar pos:
    :ivar point_property:
    :ivar interpolation: The attribute "interpolation" specifies the
        curve interpolation mechanism used for this segment. This
        mechanism uses the control points and control parameters to
        determine the position of this curve segment. For an
        GeodesicString the interpolation is fixed as "geodesic".
    """

    pos_list: Optional[PosList] = field(
        default=None,
        metadata={
            "name": "posList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    pos: List[Pos] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    point_property: List[PointProperty] = field(
        default_factory=list,
        metadata={
            "name": "pointProperty",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    interpolation: CurveInterpolationType = field(
        init=False,
        default=CurveInterpolationType.GEODESIC,
        metadata={
            "type": "Attribute",
        },
    )
