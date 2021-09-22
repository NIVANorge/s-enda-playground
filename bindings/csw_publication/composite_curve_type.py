from dataclasses import dataclass, field
from typing import List, Optional
from bindings.csw_publication.abstract_curve_segment_type import AbstractCurveSegmentType
from bindings.csw_publication.abstract_curve_type import AbstractCurveType
from bindings.csw_publication.actuate_type import ActuateType
from bindings.csw_publication.arc_1 import Arc1
from bindings.csw_publication.arc_by_bulge import ArcByBulge
from bindings.csw_publication.arc_by_center_point import ArcByCenterPoint
from bindings.csw_publication.arc_string import ArcString
from bindings.csw_publication.arc_string_by_bulge import ArcStringByBulge
from bindings.csw_publication.bezier import Bezier
from bindings.csw_publication.bspline import Bspline
from bindings.csw_publication.circle import Circle
from bindings.csw_publication.circle_by_center_point import CircleByCenterPoint
from bindings.csw_publication.clothoid import Clothoid
from bindings.csw_publication.cubic_spline import CubicSpline
from bindings.csw_publication.curve_2 import Curve2
from bindings.csw_publication.curve_segment import CurveSegment
from bindings.csw_publication.geodesic import Geodesic
from bindings.csw_publication.geodesic_string import GeodesicString
from bindings.csw_publication.length_type import LengthType
from bindings.csw_publication.line_string import LineString
from bindings.csw_publication.line_string_segment import LineStringSegment
from bindings.csw_publication.show_type import ShowType
from bindings.csw_publication.sign_type import SignType
from bindings.csw_publication.type_type import TypeType
from bindings.csw_publication.vector_type import VectorType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CompositeCurveType(AbstractCurveType):
    """
    A CompositeCurve is defined by a sequence of (orientable) curves such that
    the each curve in the sequence terminates at the start point of the
    subsequent curve in the list.

    :ivar curve_member: This element references or contains one curve in
        the composite curve. The curves are contiguous, the collection
        of curves is ordered. NOTE: This definition allows for a nested
        structure, i.e. a CompositeCurve may use, for example, another
        CompositeCurve as a curve member.
    """
    curve_member: List["CurveMember"] = field(
        default_factory=list,
        metadata={
            "name": "curveMember",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        }
    )


@dataclass
class OffsetCurveType(AbstractCurveSegmentType):
    """An offset curve is a curve at a constant distance from the basis curve.

    They can be useful as a cheap and simple alternative to constructing
    curves that are offsets by definition.

    :ivar offset_base: offsetBase is a reference to thecurve from which
        this curve is define as an offset.
    :ivar distance: distance is the distance at which the offset curve
        is generated from the basis curve. In 2D systems, positive
        distances are to be to the left of the basis curve, and the
        negative distances are to be to the right of the basis curve.
    :ivar ref_direction: refDistance is used to define the vector
        direction of the offset curve from the basis curve. It can be
        omitted in the 2D case, where the distance can be positive or
        negative. In that case, distance defines left side (positive
        distance) or right side (negative distance) with respect to the
        tangent to the basis curve. In 3D the basis curve shall have a
        well defined tangent direction for every point. The offset curve
        at any point in 3D, the basis curve shall have a well-defined
        tangent direction for every point. The offset curve at any point
        (parameter) on the basis curve c is in the direction -   -   -
        - s = v x t  where  v = c.refDirection() and - t = c.tangent() -
        For the offset direction to be well-defined, v shall not on any
        point of the curve be in the same, or opposite, direction as -
        t. The default value of the refDirection shall be the local co-
        ordinate axis vector for elevation, which indicates up for the
        curve in a geographic sense. NOTE! If the refDirection is the
        positive tangent to the local elevation axis ("points upward"),
        then the offset vector points to the left of the curve when
        viewed from above.
    """
    offset_base: Optional["CurvePropertyType"] = field(
        default=None,
        metadata={
            "name": "offsetBase",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    distance: Optional[LengthType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    ref_direction: Optional[VectorType] = field(
        default=None,
        metadata={
            "name": "refDirection",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class OrientableCurveType(AbstractCurveType):
    """OrientableCurve consists of a curve and an orientation.

    If the orientation is "+", then the OrientableCurve is identical to
    the baseCurve. If the orientation is "-", then the OrientableCurve
    is related to another _Curve with a parameterization that reverses
    the sense of the curve traversal.

    :ivar base_curve: References or contains the base curve (positive
        orientation). NOTE: This definition allows for a nested
        structure, i.e. an OrientableCurve may use another
        OrientableCurve as its base curve.
    :ivar orientation: If the orientation is "+", then the
        OrientableCurve is identical to the baseCurve. If the
        orientation is "-", then the OrientableCurve is related to
        another _Curve with a parameterization that reverses the sense
        of the curve traversal. "+" is the default value.
    """
    base_curve: Optional["BaseCurve"] = field(
        default=None,
        metadata={
            "name": "baseCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    orientation: SignType = field(
        default=SignType.VALUE,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class CompositeCurve(CompositeCurveType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class OffsetCurve(OffsetCurveType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class OrientableCurve(OrientableCurveType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class CurveSegmentArrayPropertyType:
    """
    A container for an array of curve segments.
    """
    bezier: List[Bezier] = field(
        default_factory=list,
        metadata={
            "name": "Bezier",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    bspline: List[Bspline] = field(
        default_factory=list,
        metadata={
            "name": "BSpline",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    cubic_spline: List[CubicSpline] = field(
        default_factory=list,
        metadata={
            "name": "CubicSpline",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    geodesic: List[Geodesic] = field(
        default_factory=list,
        metadata={
            "name": "Geodesic",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    geodesic_string: List[GeodesicString] = field(
        default_factory=list,
        metadata={
            "name": "GeodesicString",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    clothoid: List[Clothoid] = field(
        default_factory=list,
        metadata={
            "name": "Clothoid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    offset_curve: List[OffsetCurve] = field(
        default_factory=list,
        metadata={
            "name": "OffsetCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    circle_by_center_point: List[CircleByCenterPoint] = field(
        default_factory=list,
        metadata={
            "name": "CircleByCenterPoint",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    arc_by_center_point: List[ArcByCenterPoint] = field(
        default_factory=list,
        metadata={
            "name": "ArcByCenterPoint",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    arc_by_bulge: List[ArcByBulge] = field(
        default_factory=list,
        metadata={
            "name": "ArcByBulge",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    arc_string_by_bulge: List[ArcStringByBulge] = field(
        default_factory=list,
        metadata={
            "name": "ArcStringByBulge",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    circle: List[Circle] = field(
        default_factory=list,
        metadata={
            "name": "Circle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    arc: List[Arc1] = field(
        default_factory=list,
        metadata={
            "name": "Arc",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    arc_string: List[ArcString] = field(
        default_factory=list,
        metadata={
            "name": "ArcString",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    line_string_segment: List[LineStringSegment] = field(
        default_factory=list,
        metadata={
            "name": "LineStringSegment",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    curve_segment: List[CurveSegment] = field(
        default_factory=list,
        metadata={
            "name": "_CurveSegment",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class Segments(CurveSegmentArrayPropertyType):
    """This property element contains a list of curve segments.

    The order of the elements is significant and shall be preserved when
    processing the array.
    """
    class Meta:
        name = "segments"
        namespace = "http://www.opengis.net/gml"


@dataclass
class CurveType(AbstractCurveType):
    """Curve is a 1-dimensional primitive.

    Curves are continuous, connected, and have a measurable length in
    terms of the coordinate system. A curve is composed of one or more
    curve segments. Each curve segment within a curve may be defined
    using a different interpolation method. The curve segments are
    connected to one another, with the end point of each segment except
    the last being the start point of the next segment in the segment
    list. The orientation of the curve is positive.

    :ivar segments: This element encapsulates the segments of the curve.
    """
    segments: Optional[Segments] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )


@dataclass
class Curve1(CurveType):
    class Meta:
        name = "Curve"
        namespace = "http://www.opengis.net/gml"


@dataclass
class CurvePropertyType:
    """A property that has a curve as its value domain can either be an
    appropriate geometry element encapsulated in an element of this type or an
    XLink reference to a remote geometry element (where remote includes
    geometry elements located elsewhere in the same document).

    Either the reference or the contained element must be given, but
    neither both nor none.
    """
    orientable_curve: Optional[OrientableCurve] = field(
        default=None,
        metadata={
            "name": "OrientableCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    curve: Optional[Curve1] = field(
        default=None,
        metadata={
            "name": "Curve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    composite_curve: Optional[CompositeCurve] = field(
        default=None,
        metadata={
            "name": "CompositeCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    line_string: Optional[LineString] = field(
        default=None,
        metadata={
            "name": "LineString",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    opengis_net_gml_curve: Optional[Curve2] = field(
        default=None,
        metadata={
            "name": "_Curve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    type: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    remote_schema: Optional[str] = field(
        default=None,
        metadata={
            "name": "remoteSchema",
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class BaseCurve(CurvePropertyType):
    """This property element either references a curve via the XLink-attributes
    or contains the curve element.

    A curve element is any element which is substitutable for "_Curve".
    """
    class Meta:
        name = "baseCurve"
        namespace = "http://www.opengis.net/gml"


@dataclass
class CurveMember(CurvePropertyType):
    """This property element either references a curve via the XLink-attributes
    or contains the curve element.

    A curve element is any element which is substitutable for "_Curve".
    """
    class Meta:
        name = "curveMember"
        namespace = "http://www.opengis.net/gml"
