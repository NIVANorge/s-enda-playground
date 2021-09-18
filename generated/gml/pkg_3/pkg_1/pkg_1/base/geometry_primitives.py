from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import List, Optional
from generated.gml.pkg_3.pkg_1.pkg_1.base.basic_types import SignType
from generated.gml.pkg_3.pkg_1.pkg_1.base.geometry_basic0d1d import (
    AbstractCurveType,
    AbstractGeometricPrimitiveType,
    CurvePropertyType,
    DirectPositionType,
    VectorType,
    Coordinates,
    PointProperty,
    PointRep,
    Pos,
    PosList,
)
from generated.gml.pkg_3.pkg_1.pkg_1.base.geometry_basic2d import (
    AbstractRingType,
    AbstractSurfaceType,
    SurfacePropertyType,
    Exterior,
    InnerBoundaryIs,
    Interior,
    OuterBoundaryIs,
)
from generated.gml.pkg_3.pkg_1.pkg_1.base.geometry_complexes import CompositeSolid
from generated.gml.pkg_3.pkg_1.pkg_1.base.measures import (
    AngleType,
    LengthType,
)
from generated.gml.pkg_3.pkg_1.pkg_1.base.reference_systems import SrsName
from generated.xlink import (
    ActuateType,
    ShowType,
    TypeType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractCurveSegmentType:
    """
    Curve segment defines a homogeneous segment of a curve.

    :ivar num_derivatives_at_start: The attribute
        "numDerivativesAtStart" specifies the type of continuity between
        this curve segment and its predecessor. If this is the first
        curve segment in the curve, one of these values, as appropriate,
        is ignored. The default value of "0" means simple continuity,
        which is a mandatory minimum level of continuity. This level is
        referred to as "C 0 " in mathematical texts. A value of 1 means
        that the function and its first derivative are continuous at the
        appropriate end point: "C 1 " continuity. A value of "n" for any
        integer means the function and its first n derivatives are
        continuous: "C n " continuity. NOTE: Use of these values is only
        appropriate when the basic curve definition is an
        underdetermined system. For example, line string segments cannot
        support continuity above C 0 , since there is no spare control
        parameter to adjust the incoming angle at the end points of the
        segment. Spline functions on the other hand often have extra
        degrees of freedom on end segments that allow them to adjust the
        values of the derivatives to support C 1 or higher continuity.
    :ivar num_derivatives_at_end: The attribute "numDerivativesAtEnd"
        specifies the type of continuity between this curve segment and
        its successor. If this is the last curve segment in the curve,
        one of these values, as appropriate, is ignored. The default
        value of "0" means simple continuity, which is a mandatory
        minimum level of continuity. This level is referred to as "C 0 "
        in mathematical texts. A value of 1 means that the function and
        its first derivative are continuous at the appropriate end
        point: "C 1 " continuity. A value of "n" for any integer means
        the function and its first n derivatives are continuous: "C n "
        continuity. NOTE: Use of these values is only appropriate when
        the basic curve definition is an underdetermined system. For
        example, line string segments cannot support continuity above C
        0 , since there is no spare control parameter to adjust the
        incoming angle at the end points of the segment. Spline
        functions on the other hand often have extra degrees of freedom
        on end segments that allow them to adjust the values of the
        derivatives to support C 1 or higher continuity.
    :ivar num_derivative_interior: The attribute
        "numDerivativesInterior" specifies the type of continuity that
        is guaranteed interior to the curve. The default value of "0"
        means simple continuity, which is a mandatory minimum level of
        continuity. This level is referred to as "C 0 " in mathematical
        texts. A value of 1 means that the function and its first
        derivative are continuous at the appropriate end point: "C 1 "
        continuity. A value of "n" for any integer means the function
        and its first n derivatives are continuous: "C n " continuity.
        NOTE: Use of these values is only appropriate when the basic
        curve definition is an underdetermined system. For example, line
        string segments cannot support continuity above C 0 , since
        there is no spare control parameter to adjust the incoming angle
        at the end points of the segment. Spline functions on the other
        hand often have extra degrees of freedom on end segments that
        allow them to adjust the values of the derivatives to support C
        1 or higher continuity.
    """
    num_derivatives_at_start: int = field(
        default=0,
        metadata={
            "name": "numDerivativesAtStart",
            "type": "Attribute",
        }
    )
    num_derivatives_at_end: int = field(
        default=0,
        metadata={
            "name": "numDerivativesAtEnd",
            "type": "Attribute",
        }
    )
    num_derivative_interior: int = field(
        default=0,
        metadata={
            "name": "numDerivativeInterior",
            "type": "Attribute",
        }
    )


@dataclass
class AbstractSurfacePatchType:
    """
    A surface patch defines a homogenuous portion of a surface.
    """


class CurveInterpolationType(Enum):
    """
    CurveInterpolationType is a list of codes that may be used to identify the
    interpolation mechanisms specified by an application schema.
    """
    LINEAR = "linear"
    GEODESIC = "geodesic"
    CIRCULAR_ARC3_POINTS = "circularArc3Points"
    CIRCULAR_ARC2_POINT_WITH_BULGE = "circularArc2PointWithBulge"
    CIRCULAR_ARC_CENTER_POINT_WITH_RADIUS = "circularArcCenterPointWithRadius"
    ELLIPTICAL = "elliptical"
    CLOTHOID = "clothoid"
    CONIC = "conic"
    POLYNOMIAL_SPLINE = "polynomialSpline"
    CUBIC_SPLINE = "cubicSpline"
    RATIONAL_SPLINE = "rationalSpline"


@dataclass
class KnotType:
    """
    A knot is a breakpoint on a piecewise spline curve.

    :ivar value: The property "value" is the value of the parameter at
        the knot of the spline. The sequence of knots shall be a non-
        decreasing sequence. That is, each knot's value in the sequence
        shall be equal to or greater than the previous knot's value. The
        use of equal consecutive knots is normally handled using the
        multiplicity.
    :ivar multiplicity: The property "multiplicity" is the multiplicity
        of this knot used in the definition of the spline (with the same
        weight).
    :ivar weight: The property "weight" is the value of the averaging
        weight used for this knot of the spline.
    """
    value: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    multiplicity: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    weight: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )


class KnotTypesType(Enum):
    """Defines allowed values for the knots` type.

    Uniform knots implies that all knots are of multiplicity 1 and they
    differ by a positive constant from the preceding knot. Knots are
    quasi-uniform iff they are of multiplicity (degree + 1) at the ends,
    of multiplicity 1 elsewhere, and they differ by a positive constant
    from the preceding knot.
    """
    UNIFORM = "uniform"
    QUASI_UNIFORM = "quasiUniform"
    PIECEWISE_BEZIER = "piecewiseBezier"


class SurfaceInterpolationType(Enum):
    """
    SurfaceInterpolationType is a list of codes that may be used to identify
    the interpolation mechanisms specified by an application schema.
    """
    NONE = "none"
    PLANAR = "planar"
    SPHERICAL = "spherical"
    ELLIPTICAL = "elliptical"
    CONIC = "conic"
    TIN = "tin"
    PARAMETRIC_CURVE = "parametricCurve"
    POLYNOMIAL_SPLINE = "polynomialSpline"
    RATIONAL_SPLINE = "rationalSpline"
    TRIANGULATED_SPLINE = "triangulatedSpline"


@dataclass
class AbstractParametricCurveSurfaceType(AbstractSurfacePatchType):
    pass


@dataclass
class AbstractSolidType(AbstractGeometricPrimitiveType):
    """An abstraction of a solid to support the different levels of complexity.

    A solid is always contiguous.
    """


@dataclass
class AffinePlacementType:
    """A placement takes a standard geometric construction and places it in
    geographic space.

    It defines a
    transformation from a constructive parameter space to the
    co-ordinate space of the co-ordinate reference system being used.
    Parameter spaces in formulae in this International Standard are
    given as (u, v) in 2D and(u, v, w) in 3D. Co-ordinate reference
    systems positions are given in formulae, in this International
    Standard, by either (x, y) in 2D, or (x, y, z) in 3D.
    Affine placements are defined by linear transformations from
    parameter space to the target co-ordiante space. 2-dimensional
    Cartesian parameter space,(u,v) transforms into 3-dimensional co-
    ordinate reference systems,(x,y,z) by using an affine
    transformation,(u,v)-&gt;(x,y,z) which is defined :
    x       ux vx   x0
    u
    y =     uy vy   + y0
    v
    x       uz vz   z0
    Then, given this equation, the location element of the
    AffinePlacement is the direct position (x0, y0, z0), which is the
    target position of the origin in (u, v). The two reference
    directions (ux, uy, uz) and (vx, vy, vz) are the target
    directions of the unit vectors at the origin in (u, v).

    :ivar location: The location property gives the target of the
        parameter space origin. This is the vector (x0, y0, z0) in the
        formulae above.
    :ivar ref_direction: The attribute refDirection gives the target
        directions for the co-ordinate basis vectors of the parameter
        space. These are the columns of the matrix in the formulae given
        above. The number of directions given shall be inDimension. The
        dimension of the directions shall be outDimension.
    :ivar in_dimension: Dimension of the constructive parameter space.
    :ivar out_dimension: Dimension of the co-ordinate space.
    """
    location: Optional[DirectPositionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    ref_direction: List[VectorType] = field(
        default_factory=list,
        metadata={
            "name": "refDirection",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        }
    )
    in_dimension: Optional[int] = field(
        default=None,
        metadata={
            "name": "inDimension",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    out_dimension: Optional[int] = field(
        default=None,
        metadata={
            "name": "outDimension",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )


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


@dataclass
class ArcStringByBulgeType(AbstractCurveSegmentType):
    """This variant of the arc computes the mid points of the arcs instead of
    storing the coordinates directly.

    The control point sequence consists of the start and end points of
    each arc plus the bulge.

    :ivar pos:
    :ivar point_property:
    :ivar point_rep: Deprecated with GML version 3.1.0. Use
        "pointProperty" instead. Included for backwards compatibility
        with GML 3.0.0.
    :ivar pos_list:
    :ivar coordinates: Deprecated with GML version 3.1.0. Use "posList"
        instead.
    :ivar bulge: The bulge controls the offset of each arc's midpoint.
        The "bulge" is the real number multiplier for the normal that
        determines the offset direction of the midpoint of each arc. The
        length of the bulge sequence is exactly 1 less than the length
        of the control point array, since a bulge is needed for each
        pair of adjacent points in the control point array. The bulge is
        not given by a distance, since it is simply a multiplier for the
        normal. The midpoint of the resulting arc is given by: midPoint
        = ((startPoint + endPoint)/2.0) + bulge*normal
    :ivar normal: The attribute "normal" is a vector normal
        (perpendicular) to the chord of the arc, the line joining the
        first and last point of the arc. In a 2D coordinate system,
        there are only two possible directions for the normal, and it is
        often given as a signed real, indicating its length, with a
        positive sign indicating a left turn angle from the chord line,
        and a negative sign indicating a right turn from the chord. In
        3D, the normal determines the plane of the arc, along with the
        start and endPoint of the arc. The normal is usually a unit
        vector, but this is not absolutely necessary. If the normal is a
        zero vector, the geometric object becomes equivalent to the
        straight line between the two end points. The length of the
        normal sequence is exactly the same as for the bulge sequence, 1
        less than the control point sequence length.
    :ivar interpolation: The attribute "interpolation" specifies the
        curve interpolation mechanism used for this segment. This
        mechanism uses the control points and control parameters to
        determine the position of this curve segment. For an
        ArcStringByBulge the interpolation is fixed as
        "circularArc2PointWithBulge".
    :ivar num_arc: The number of arcs in the arc string can be
        explicitly stated in this attribute. The number of control
        points in the arc string must be numArc + 1.
    """
    pos: List[Pos] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 2,
            "sequential": True,
        }
    )
    point_property: List[PointProperty] = field(
        default_factory=list,
        metadata={
            "name": "pointProperty",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 2,
            "sequential": True,
        }
    )
    point_rep: List[PointRep] = field(
        default_factory=list,
        metadata={
            "name": "pointRep",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 2,
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
    bulge: List[float] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        }
    )
    normal: List[VectorType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        }
    )
    interpolation: CurveInterpolationType = field(
        init=False,
        default=CurveInterpolationType.CIRCULAR_ARC2_POINT_WITH_BULGE,
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


@dataclass
class CubicSplineType(AbstractCurveSegmentType):
    """Cubic splines are similar to line strings in that they are a sequence of
    segments each with its own defining function.

    A cubic spline uses the control points and a set of derivative parameters to define a piecewise 3rd degree polynomial interpolation. Unlike line-strings, the parameterization by arc length is not necessarily still a polynomial.
    The function describing the curve must be C2, that is, have a continuous 1st and 2nd derivative at all points, and pass through the controlPoints in the order given. Between the control points, the curve segment is defined by a cubic polynomial. At each control point, the polynomial changes in such a manner that the 1st and 2nd derivative vectors are the same from either side. The control parameters record must contain vectorAtStart, and vectorAtEnd which are the unit tangent vectors at controlPoint[1] and controlPoint[n] where n = controlPoint.count.
    Note: only the direction of the vectors is relevant, not their length.

    :ivar pos:
    :ivar point_property:
    :ivar point_rep: Deprecated with GML version 3.1.0. Use
        "pointProperty" instead. Included for backwards compatibility
        with GML 3.0.0.
    :ivar pos_list:
    :ivar coordinates: Deprecated with GML version 3.1.0. Use "posList"
        instead.
    :ivar vector_at_start: "vectorAtStart" is the unit tangent vector at
        the start point of the spline.
    :ivar vector_at_end: "vectorAtEnd" is the unit tangent vector at the
        end point of the spline.
    :ivar interpolation: The attribute "interpolation" specifies the
        curve interpolation mechanism used for this segment. This
        mechanism uses the control points and control parameters to
        determine the position of this curve segment. For a CubicSpline
        the interpolation is fixed as "cubicSpline".
    :ivar degree: The degree for a cubic spline is "3".
    """
    pos: List[Pos] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 2,
            "sequential": True,
        }
    )
    point_property: List[PointProperty] = field(
        default_factory=list,
        metadata={
            "name": "pointProperty",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 2,
            "sequential": True,
        }
    )
    point_rep: List[PointRep] = field(
        default_factory=list,
        metadata={
            "name": "pointRep",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 2,
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
    vector_at_start: Optional[VectorType] = field(
        default=None,
        metadata={
            "name": "vectorAtStart",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    vector_at_end: Optional[VectorType] = field(
        default=None,
        metadata={
            "name": "vectorAtEnd",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    interpolation: CurveInterpolationType = field(
        init=False,
        default=CurveInterpolationType.CUBIC_SPLINE,
        metadata={
            "type": "Attribute",
        }
    )
    degree: int = field(
        init=False,
        default=3,
        metadata={
            "type": "Attribute",
        }
    )


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
    interpolation: CurveInterpolationType = field(
        init=False,
        default=CurveInterpolationType.GEODESIC,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class KnotPropertyType:
    """
    Encapsulates a knot to use it in a geometric type.
    """
    knot: Optional[KnotType] = field(
        default=None,
        metadata={
            "name": "Knot",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )


@dataclass
class LineStringSegmentType(AbstractCurveSegmentType):
    """A LineStringSegment is a curve segment that is defined by two or more
    coordinate tuples, with linear interpolation between them.

    Note: LineStringSegment implements GM_LineString of ISO 19107.

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
        determine the position of this curve segment. For a
        LineStringSegment the interpolation is fixed as "linear".
    """
    pos: List[Pos] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 2,
            "sequential": True,
        }
    )
    point_property: List[PointProperty] = field(
        default_factory=list,
        metadata={
            "name": "pointProperty",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 2,
            "sequential": True,
        }
    )
    point_rep: List[PointRep] = field(
        default_factory=list,
        metadata={
            "name": "pointRep",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 2,
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
        default=CurveInterpolationType.LINEAR,
        metadata={
            "type": "Attribute",
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
class OrientableSurfaceType(AbstractSurfaceType):
    """OrientableSurface consists of a surface and an orientation.

    If the orientation is "+", then the OrientableSurface is identical
    to the baseSurface. If the orientation is "-", then the
    OrientableSurface is a reference to a Surface with an up-normal that
    reverses the direction for this OrientableSurface, the sense of "the
    top of the surface".

    :ivar base_surface: References or contains the base surface
        (positive orientation).
    :ivar orientation: If the orientation is "+", then the
        OrientableSurface is identical to the baseSurface. If the
        orientation is "-", then the OrientableSurface is a reference to
        a Surface with an up-normal that reverses the direction for this
        OrientableSurface, the sense of "the top of the surface". "+" is
        the default value.
    """
    base_surface: Optional["BaseSurface"] = field(
        default=None,
        metadata={
            "name": "baseSurface",
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
class PolygonPatchType(AbstractSurfacePatchType):
    """A PolygonPatch is a surface patch that is defined by a set of boundary
    curves and an underlying surface to which these curves adhere.

    The curves are coplanar and the polygon uses planar interpolation in
    its interior. Implements GM_Polygon of ISO 19107.

    :ivar outer_boundary_is:
    :ivar exterior:
    :ivar inner_boundary_is:
    :ivar interior:
    :ivar interpolation: The attribute "interpolation" specifies the
        interpolation mechanism used for this surface patch. Currently
        only planar surface patches are defined in GML 3, the attribute
        is fixed to "planar", i.e. the interpolation method shall return
        points on a single plane. The boundary of the patch shall be
        contained within that plane.
    """
    outer_boundary_is: Optional[OuterBoundaryIs] = field(
        default=None,
        metadata={
            "name": "outerBoundaryIs",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    exterior: Optional[Exterior] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    inner_boundary_is: List[InnerBoundaryIs] = field(
        default_factory=list,
        metadata={
            "name": "innerBoundaryIs",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    interior: List[Interior] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    interpolation: SurfaceInterpolationType = field(
        init=False,
        default=SurfaceInterpolationType.PLANAR,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class RectangleType(AbstractSurfacePatchType):
    """Represents a rectangle as a surface with an outer boundary consisting of
    a linear ring.

    Note that this is a polygon (subtype) with no inner boundaries. The
    number of points in the linear ring must be five.

    :ivar outer_boundary_is:
    :ivar exterior: Constraint: The Ring shall be a LinearRing and must
        form a rectangle; the first and the last position must be co-
        incident.
    :ivar interpolation: The attribute "interpolation" specifies the
        interpolation mechanism used for this surface patch. Currently
        only planar surface patches are defined in GML 3, the attribute
        is fixed to "planar", i.e. the interpolation method shall return
        points on a single plane. The boundary of the patch shall be
        contained within that plane.
    """
    outer_boundary_is: Optional[OuterBoundaryIs] = field(
        default=None,
        metadata={
            "name": "outerBoundaryIs",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    exterior: Optional[Exterior] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    interpolation: SurfaceInterpolationType = field(
        init=False,
        default=SurfaceInterpolationType.PLANAR,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class TriangleType(AbstractSurfacePatchType):
    """Represents a triangle as a surface with an outer boundary consisting of
    a linear ring.

    Note that this is a polygon (subtype) with no inner boundaries. The
    number of points in the linear ring must be four.

    :ivar outer_boundary_is:
    :ivar exterior: Constraint: The Ring shall be a LinearRing and must
        form a triangle, the first and the last position must be co-
        incident.
    :ivar interpolation: The attribute "interpolation" specifies the
        interpolation mechanism used for this surface patch. Currently
        only planar surface patches are defined in GML 3, the attribute
        is fixed to "planar", i.e. the interpolation method shall return
        points on a single plane. The boundary of the patch shall be
        contained within that plane.
    """
    outer_boundary_is: Optional[OuterBoundaryIs] = field(
        default=None,
        metadata={
            "name": "outerBoundaryIs",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    exterior: Optional[Exterior] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    interpolation: SurfaceInterpolationType = field(
        init=False,
        default=SurfaceInterpolationType.PLANAR,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class CurveSegment(AbstractCurveSegmentType):
    """
    The "_CurveSegment" element is the abstract head of the substituition group
    for all curve segment elements, i.e. continuous segments of the same
    interpolation mechanism.
    """
    class Meta:
        name = "_CurveSegment"
        namespace = "http://www.opengis.net/gml"


@dataclass
class SurfacePatch(AbstractSurfacePatchType):
    """
    The "_SurfacePatch" element is the abstract head of the substituition group
    for all surface pach elements describing a continuous portion of a surface.
    """
    class Meta:
        name = "_SurfacePatch"
        namespace = "http://www.opengis.net/gml"


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
class BaseSurface(SurfacePropertyType):
    """This property element either references a surface via the XLink-
    attributes or contains the surface element.

    A surface element is any element which is substitutable for
    "_Surface".
    """
    class Meta:
        name = "baseSurface"
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


@dataclass
class AbstractGriddedSurfaceType(AbstractParametricCurveSurfaceType):
    """A gridded surface is a parametric curve surface derived from a
    rectangular grid in the parameter space.

    The rows from this grid are control points for
    horizontal surface curves; the columns are control points
    for vertical surface curves. The working assumption is that
    for a pair of parametric co-ordinates (s, t) that the
    horizontal curves for each integer offset are calculated
    and evaluated at "s". The defines a sequence of control
    points:
    cn(s) : s  1 .....columns
    From this sequence a vertical curve is calculated for "s",
    and evaluated at "t". In most cases, the order of
    calculation (horizontal-vertical vs. vertical-horizontal)
    does not make a difference. Where it does, the horizontal-
    vertical order shall be the one used.
    Logically, any pair of curve interpolation types can lead
    to a subtype of GriddedSurface. The following clauses
    define some most commonly encountered surfaces that can
    be represented in this manner.

    :ivar row:
    :ivar rows: The attribute rows gives the number of rows in the
        parameter grid.
    :ivar columns: The attribute columns gives the number of columns in
        the parameter grid.
    """
    row: List["AbstractGriddedSurfaceType.Row"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        }
    )
    rows: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    columns: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )

    @dataclass
    class Row:
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


@dataclass
class AffinePlacement(AffinePlacementType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class ArcByBulgeType(ArcStringByBulgeType):
    """
    An ArcByBulge is an arc string with only one arc unit, i.e. two control
    points and one bulge.

    :ivar num_arc: An arc is an arc string consiting of a single arc,
        the attribute is fixed to "1".
    """
    num_arc: int = field(
        init=False,
        default=1,
        metadata={
            "name": "numArc",
            "type": "Attribute",
        }
    )


@dataclass
class ArcByCenterPoint(ArcByCenterPointType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class ArcString(ArcStringType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class ArcStringByBulge(ArcStringByBulgeType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class ArcType(ArcStringType):
    """
    An Arc is an arc string with only one arc unit, i.e. three control points.

    :ivar num_arc: An arc is an arc string consiting of a single arc,
        the attribute is fixed to "1".
    """
    num_arc: int = field(
        init=False,
        default=1,
        metadata={
            "name": "numArc",
            "type": "Attribute",
        }
    )


@dataclass
class BsplineType(AbstractCurveSegmentType):
    """A B-Spline is a piecewise parametric polynomial or rational curve
    described in terms of control points and basis functions.

    Knots are breakpoints on the curve that connect its pieces. They are
    given as a non-decreasing sequence of real numbers. If the weights
    in the knots are equal then it is a polynomial spline. The degree is
    the algebraic degree of the basis functions.

    :ivar pos:
    :ivar point_property:
    :ivar point_rep: Deprecated with GML version 3.1.0. Use
        "pointProperty" instead. Included for backwards compatibility
        with GML 3.0.0.
    :ivar pos_list:
    :ivar coordinates: Deprecated with GML version 3.1.0. Use "posList"
        instead.
    :ivar degree: The attribute "degree" shall be the degree of the
        polynomial used for interpolation in this spline.
    :ivar knot: The property "knot" shall be the sequence of distinct
        knots used to define the spline basis functions.
    :ivar interpolation: The attribute "interpolation" specifies the
        curve interpolation mechanism used for this segment. This
        mechanism uses the control points and control parameters to
        determine the position of this curve segment. For a BSpline the
        interpolation can be either "polynomialSpline" or
        "rationalSpline", default is "polynomialSpline".
    :ivar is_polynomial: The attribute isPolynomial is set to true if
        this is a polynomial spline.
    :ivar knot_type: The attribute "knotType" gives the type of knot
        distribution used in defining this spline. This is for
        information only and is set according to the different
        construction-functions.
    """
    class Meta:
        name = "BSplineType"

    pos: List[Pos] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        }
    )
    point_property: List[PointProperty] = field(
        default_factory=list,
        metadata={
            "name": "pointProperty",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        }
    )
    point_rep: List[PointRep] = field(
        default_factory=list,
        metadata={
            "name": "pointRep",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
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
    degree: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    knot: List[KnotPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 2,
        }
    )
    interpolation: CurveInterpolationType = field(
        default=CurveInterpolationType.POLYNOMIAL_SPLINE,
        metadata={
            "type": "Attribute",
        }
    )
    is_polynomial: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isPolynomial",
            "type": "Attribute",
        }
    )
    knot_type: Optional[KnotTypesType] = field(
        default=None,
        metadata={
            "name": "knotType",
            "type": "Attribute",
        }
    )


@dataclass
class CircleByCenterPointType(ArcByCenterPointType):
    """A CircleByCenterPoint is an ArcByCenterPoint with identical start and
    end angle to form a full circle.

    Again, this represenation can be used only in 2D.
    """


@dataclass
class CubicSpline(CubicSplineType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class GeodesicString(GeodesicStringType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class GeodesicType(GeodesicStringType):
    """A Geodesic consists of two distinct positions joined by a geodesic
    curve.

    The control points of a Geodesic shall lie on the geodesic between
    its start point and end points. Between these two points, a geodesic
    curve defined from ellipsoid or geoid model used by the co-ordinate
    reference systems may be used to interpolate other positions. Any
    other point in the controlPoint array must fall on this geodesic.
    """


@dataclass
class LineStringSegment(LineStringSegmentType):
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
class OrientableSurface(OrientableSurfaceType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class PolygonPatch(PolygonPatchType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class Rectangle(RectangleType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class RingType(AbstractRingType):
    """A Ring is used to represent a single connected component of a surface
    boundary.

    It consists of a sequence of curves connected in a cycle (an object whose boundary is empty).
    A Ring is structurally similar to a composite curve in that the endPoint of each curve in the sequence is the startPoint of the next curve in the Sequence. Since the sequence is circular, there is no exception to this rule. Each ring, like all boundaries, is a cycle and each ring is simple.
    NOTE: Even though each Ring is simple, the boundary need not be simple. The easiest case of this is where one of the interior rings of a surface is tangent to its exterior ring.

    :ivar curve_member: This element references or contains one curve in
        the composite curve. The curves are contiguous, the collection
        of curves is ordered. NOTE: This definition allows for a nested
        structure, i.e. a CompositeCurve may use, for example, another
        CompositeCurve as a curve member.
    """
    curve_member: List[CurveMember] = field(
        default_factory=list,
        metadata={
            "name": "curveMember",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        }
    )


@dataclass
class SolidType(AbstractSolidType):
    """A solid is the basis for 3-dimensional geometry.

    The extent of a solid is defined by the boundary surfaces (shells).
    A shell is represented by a composite surface, where every  shell is
    used to represent a single connected component of the boundary of a
    solid. It consists of a composite surface (a list of orientable
    surfaces) connected in a topological cycle (an object whose boundary
    is empty). Unlike a Ring, a Shell's elements have no natural sort
    order. Like Rings, Shells are simple.

    :ivar exterior: Boundaries of solids are similar to surface
        boundaries. In normal 3-dimensional Euclidean space, one
        (composite) surface is distinguished as the exterior. In the
        more general case, this is not always possible.
    :ivar interior: Boundaries of solids are similar to surface
        boundaries.
    """
    exterior: Optional[SurfacePropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    interior: List[SurfacePropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class Triangle(TriangleType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class ParametricCurveSurface(AbstractParametricCurveSurfaceType):
    class Meta:
        name = "_ParametricCurveSurface"
        namespace = "http://www.opengis.net/gml"


@dataclass
class Solid2(AbstractSolidType):
    """
    The "_Solid" element is the abstract head of the substituition group for
    all (continuous) solid elements.
    """
    class Meta:
        name = "_Solid"
        namespace = "http://www.opengis.net/gml"


@dataclass
class Arc(ArcType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class ArcByBulge(ArcByBulgeType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class Bspline(BsplineType):
    class Meta:
        name = "BSpline"
        namespace = "http://www.opengis.net/gml"


@dataclass
class BezierType(BsplineType):
    """Bezier curves are polynomial splines that use Bezier or Bernstein
    polynomials for interpolation purposes.

    It is a special case of the B-Spline curve with two knots.

    :ivar interpolation: The attribute "interpolation" specifies the
        curve interpolation mechanism used for this segment. This
        mechanism uses the control points and control parameters to
        determine the position of this curve segment. For a Bezier the
        interpolation is fixed as "polynomialSpline".
    :ivar is_polynomial: The attribute isPolynomial is set to true as
        this is a polynomial spline.
    """
    interpolation: CurveInterpolationType = field(
        init=False,
        default=CurveInterpolationType.POLYNOMIAL_SPLINE,
        metadata={
            "type": "Attribute",
        }
    )
    is_polynomial: bool = field(
        init=False,
        default=True,
        metadata={
            "name": "isPolynomial",
            "type": "Attribute",
        }
    )


@dataclass
class CircleByCenterPoint(CircleByCenterPointType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class CircleType(ArcType):
    """A Circle is an arc whose ends coincide to form a simple closed loop.

    The "start" and "end" bearing are equal and shall be the bearing for
    the first controlPoint listed. The three control points must be
    distinct non-co-linear points for the Circle to be unambiguously
    defined. The arc is simply extended past the third control point
    until the first control point is encountered.
    """


@dataclass
class ClothoidType(AbstractCurveSegmentType):
    """A clothoid, or Cornu's spiral, is plane curve whose curvature is a fixed
    function of its length.

    In suitably chosen co-ordinates it is given by Fresnel's
    integrals.
    x(t) = 0-integral-t cos(AT*T/2)dT
    y(t) = 0-integral-t sin(AT*T/2)dT
    This geometry is mainly used as a transition curve between
    curves of type straight line to circular arc or circular arc
    to circular arc. With this curve type it is possible to
    achieve a C2-continous transition between the above mentioned
    curve types. One formula for the Clothoid is A*A = R*t where
    A is constant, R is the varying radius of curvature along the
    the curve and t is the length along and given in the Fresnel
    integrals.

    :ivar ref_location:
    :ivar scale_factor: The element gives the value for the constant in
        the Fresnel's integrals.
    :ivar start_parameter: The startParameter is the arc length distance
        from the inflection point that will be the start point for this
        curve segment. This shall be lower limit used in the Fresnel
        integral and is the value of the constructive parameter of this
        curve segment at its start point. The startParameter can either
        be positive or negative. NOTE! If 0.0 (zero), lies between the
        startParameter and the endParameter of the clothoid, then the
        curve goes through the clothoid's inflection point, and the
        direction of its radius of curvature, given by the second
        derivative vector, changes sides with respect to the tangent
        vector. The term length distance for the
    :ivar end_parameter: The endParameter is the arc length distance
        from the inflection point that will be the end point for this
        curve segment. This shall be upper limit used in the Fresnel
        integral and is the value of the constructive parameter of this
        curve segment at its start point. The startParameter can either
        be positive or negative.
    """
    ref_location: Optional["ClothoidType.RefLocation"] = field(
        default=None,
        metadata={
            "name": "refLocation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    scale_factor: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "scaleFactor",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    start_parameter: Optional[float] = field(
        default=None,
        metadata={
            "name": "startParameter",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    end_parameter: Optional[float] = field(
        default=None,
        metadata={
            "name": "endParameter",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )

    @dataclass
    class RefLocation:
        """
        :ivar affine_placement: The "refLocation" is an affine mapping
            that places  the curve defined by the Fresnel Integrals into
            the co-ordinate reference system of this object.
        """
        affine_placement: Optional[AffinePlacement] = field(
            default=None,
            metadata={
                "name": "AffinePlacement",
                "type": "Element",
                "namespace": "http://www.opengis.net/gml",
                "required": True,
            }
        )


@dataclass
class ConeType(AbstractGriddedSurfaceType):
    """A cone is a gridded surface given as a family of conic sections whose
    control points vary linearly.

    NOTE! A 5-point ellipse with all defining positions identical is a
    point. Thus, a truncated elliptical cone can be given as a 2x5 set
    of control points ((P1, P1, P1, P1, P1), (P2, P3, P4, P5, P6)). P1
    is the apex of the cone. P2, P3,P4, P5 and P6 are any five distinct
    points around the base ellipse of the cone. If the horizontal curves
    are circles as opposed to ellipses, the a circular cone can be
    constructed using ((P1, P1, P1),(P2, P3, P4)). The apex most not
    coinside with the other plane.
    """
    horizontal_curve_type: CurveInterpolationType = field(
        init=False,
        default=CurveInterpolationType.CIRCULAR_ARC3_POINTS,
        metadata={
            "name": "horizontalCurveType",
            "type": "Attribute",
        }
    )
    vertical_curve_type: CurveInterpolationType = field(
        init=False,
        default=CurveInterpolationType.LINEAR,
        metadata={
            "name": "verticalCurveType",
            "type": "Attribute",
        }
    )


@dataclass
class CylinderType(AbstractGriddedSurfaceType):
    """A cylinder is a gridded surface given as a family of circles whose
    positions vary along a set of parallel lines, keeping the cross sectional
    horizontal curves of a constant shape.

    NOTE! Given the same working assumptions as in the previous note, a
    Cylinder can be given by two circles, giving us the control points
    of the form ((P1, P2, P3),(P4, P5, P6)).
    """
    horizontal_curve_type: CurveInterpolationType = field(
        init=False,
        default=CurveInterpolationType.CIRCULAR_ARC3_POINTS,
        metadata={
            "name": "horizontalCurveType",
            "type": "Attribute",
        }
    )
    vertical_curve_type: CurveInterpolationType = field(
        init=False,
        default=CurveInterpolationType.LINEAR,
        metadata={
            "name": "verticalCurveType",
            "type": "Attribute",
        }
    )


@dataclass
class Geodesic(GeodesicType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


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


@dataclass
class Ring1(RingType):
    class Meta:
        name = "Ring"
        namespace = "http://www.opengis.net/gml"


@dataclass
class Solid1(SolidType):
    class Meta:
        name = "Solid"
        namespace = "http://www.opengis.net/gml"


@dataclass
class SphereType(AbstractGriddedSurfaceType):
    """A sphere is a gridded surface given as a family of circles whose
    positions vary linearly along the axis of the sphere, and whise radius
    varies in proportions to the cosine function of the central angle.

    The horizontal
    circles resemble lines of constant latitude, and the vertical
    arcs resemble lines of constant longitude.
    NOTE! If the control points are sorted in terms of increasing
    longitude, and increasing latitude, the upNormal of a sphere
    is the outward normal.
    EXAMPLE If we take a gridded set of latitudes and longitudes
    in degrees,(u,v) such as
    (-90,-180)  (-90,-90)  (-90,0)  (-90,  90) (-90, 180)
    (-45,-180)  (-45,-90)  (-45,0)  (-45,  90) (-45, 180)
    (  0,-180)  (  0,-90)  (  0,0)  (  0,  90) (  0, 180)
    ( 45,-180)  ( 45,-90)  ( 45,0)  ( 45, -90) ( 45, 180)
    ( 90,-180)  ( 90,-90)  ( 90,0)  ( 90, -90) ( 90, 180)
    And map these points to 3D using the usual equations (where R
    is the radius of the required sphere).
    z = R sin u
    x = (R cos u)(sin v)
    y = (R cos u)(cos v)
    We have a sphere of Radius R, centred at (0,0), as a gridded
    surface. Notice that the entire first row and the entire last
    row of the control points map to a single point in each 3D
    Euclidean space, North and South poles respectively, and that
    each horizontal curve closes back on itself forming a
    geometric cycle. This gives us a metrically bounded (of finite
    size), topologically unbounded (not having a boundary, a
    cycle) surface.
    """
    horizontal_curve_type: CurveInterpolationType = field(
        init=False,
        default=CurveInterpolationType.CIRCULAR_ARC3_POINTS,
        metadata={
            "name": "horizontalCurveType",
            "type": "Attribute",
        }
    )
    vertical_curve_type: CurveInterpolationType = field(
        init=False,
        default=CurveInterpolationType.CIRCULAR_ARC3_POINTS,
        metadata={
            "name": "verticalCurveType",
            "type": "Attribute",
        }
    )


@dataclass
class GriddedSurface(AbstractGriddedSurfaceType):
    class Meta:
        name = "_GriddedSurface"
        namespace = "http://www.opengis.net/gml"


@dataclass
class Bezier(BezierType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class Circle(CircleType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class Clothoid(ClothoidType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class Cone(ConeType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class Cylinder(CylinderType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class RingPropertyType:
    """
    Encapsulates a ring to represent properties in features or geometry
    collections.
    """
    ring: Optional[Ring1] = field(
        default=None,
        metadata={
            "name": "Ring",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )


@dataclass
class SolidArrayPropertyType:
    """A container for an array of solids.

    The elements are always contained in the array property, referencing
    geometry elements or arrays of geometry elements is not supported.
    """
    solid: List[Solid1] = field(
        default_factory=list,
        metadata={
            "name": "Solid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        }
    )
    composite_solid: List[CompositeSolid] = field(
        default_factory=list,
        metadata={
            "name": "CompositeSolid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        }
    )
    opengis_net_gml_solid: List[Solid2] = field(
        default_factory=list,
        metadata={
            "name": "_Solid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        }
    )


@dataclass
class SolidPropertyType:
    """A property that has a solid as its value domain can either be an
    appropriate geometry element encapsulated in an element of this type or an
    XLink reference to a remote geometry element (where remote includes
    geometry elements located elsewhere in the same document).

    Either the reference or the contained element must be given, but
    neither both nor none.
    """
    solid: Optional[Solid1] = field(
        default=None,
        metadata={
            "name": "Solid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    composite_solid: Optional[CompositeSolid] = field(
        default=None,
        metadata={
            "name": "CompositeSolid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    opengis_net_gml_solid: Optional[Solid2] = field(
        default=None,
        metadata={
            "name": "_Solid",
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
class Sphere(SphereType):
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
    arc: List[Arc] = field(
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
class SurfacePatchArrayPropertyType:
    """
    A container for an array of surface patches.
    """
    sphere: List[Sphere] = field(
        default_factory=list,
        metadata={
            "name": "Sphere",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        }
    )
    cylinder: List[Cylinder] = field(
        default_factory=list,
        metadata={
            "name": "Cylinder",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        }
    )
    cone: List[Cone] = field(
        default_factory=list,
        metadata={
            "name": "Cone",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        }
    )
    gridded_surface: List[GriddedSurface] = field(
        default_factory=list,
        metadata={
            "name": "_GriddedSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        }
    )
    parametric_curve_surface: List[ParametricCurveSurface] = field(
        default_factory=list,
        metadata={
            "name": "_ParametricCurveSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        }
    )
    rectangle: List[Rectangle] = field(
        default_factory=list,
        metadata={
            "name": "Rectangle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        }
    )
    triangle: List[Triangle] = field(
        default_factory=list,
        metadata={
            "name": "Triangle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        }
    )
    polygon_patch: List[PolygonPatch] = field(
        default_factory=list,
        metadata={
            "name": "PolygonPatch",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        }
    )
    surface_patch: List[SurfacePatch] = field(
        default_factory=list,
        metadata={
            "name": "_SurfacePatch",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        }
    )


@dataclass
class SolidArrayProperty(SolidArrayPropertyType):
    class Meta:
        name = "solidArrayProperty"
        namespace = "http://www.opengis.net/gml"


@dataclass
class SolidProperty(SolidPropertyType):
    """This property element either references a solid via the XLink-attributes
    or contains the solid element.

    solidProperty is the predefined property which can be used by GML
    Application Schemas whenever a GML Feature has a property with a
    value that is substitutable for _Solid.
    """
    class Meta:
        name = "solidProperty"
        namespace = "http://www.opengis.net/gml"


@dataclass
class PolygonPatchArrayPropertyType(SurfacePatchArrayPropertyType):
    """
    This type defines a container for an array of polygon patches.
    """


@dataclass
class TrianglePatchArrayPropertyType(SurfacePatchArrayPropertyType):
    """
    This type defines a container for an array of triangle patches.
    """


@dataclass
class Patches(SurfacePatchArrayPropertyType):
    """This property element contains a list of surface patches.

    The order of the elements is significant and shall be preserved when
    processing the array.
    """
    class Meta:
        name = "patches"
        namespace = "http://www.opengis.net/gml"


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
class PolygonPatches(PolygonPatchArrayPropertyType):
    """This property element contains a list of polygon patches.

    The order of the patches is significant and shall be preserved when
    processing the list.
    """
    class Meta:
        name = "polygonPatches"
        namespace = "http://www.opengis.net/gml"


@dataclass
class TrianglePatches(TrianglePatchArrayPropertyType):
    """This property element contains a list of triangle patches.

    The order of the patches is significant and shall be preserved when
    processing the list.
    """
    class Meta:
        name = "trianglePatches"
        namespace = "http://www.opengis.net/gml"


@dataclass
class Curve1(CurveType):
    class Meta:
        name = "Curve"
        namespace = "http://www.opengis.net/gml"


@dataclass
class SurfaceType(AbstractSurfaceType):
    """A Surface is a 2-dimensional primitive and is composed of one or more
    surface patches.

    The surface patches are connected to one another. The orientation of
    the surface is positive ("up"). The orientation of a surface chooses
    an "up" direction through the choice of the upward normal, which, if
    the surface is not a cycle, is the side of the surface from which
    the exterior boundary appears counterclockwise. Reversal of the
    surface orientation reverses the curve orientation of each boundary
    component, and interchanges the conceptual "up" and "down" direction
    of the surface. If the surface is the boundary of a solid, the "up"
    direction is usually outward. For closed surfaces, which have no
    boundary, the up direction is that of the surface patches, which
    must be consistent with one another. Its included surface patches
    describe the interior structure of the Surface.

    :ivar triangle_patches:
    :ivar polygon_patches:
    :ivar patches: This element encapsulates the patches of the surface.
    """
    triangle_patches: Optional[TrianglePatches] = field(
        default=None,
        metadata={
            "name": "trianglePatches",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    polygon_patches: Optional[PolygonPatches] = field(
        default=None,
        metadata={
            "name": "polygonPatches",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    patches: Optional[Patches] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class PolyhedralSurfaceType(SurfaceType):
    """A polyhedral surface is a surface composed of polygon surfaces connected
    along their common boundary curves.

    This differs from the surface type only in the restriction on the
    types of surface patches acceptable.
    """
    srs_name: List[SrsName] = field(
        default_factory=list,
        metadata={
            "name": "srsName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class Surface1(SurfaceType):
    class Meta:
        name = "Surface"
        namespace = "http://www.opengis.net/gml"


@dataclass
class TriangulatedSurfaceType(SurfaceType):
    """A triangulated surface is a polyhedral surface that is composed only of
    triangles.

    There is no restriction on how the triangulation is derived.
    """
    srs_name: List[SrsName] = field(
        default_factory=list,
        metadata={
            "name": "srsName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class PolyhedralSurface(PolyhedralSurfaceType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class TinType(TriangulatedSurfaceType):
    """A tin is a triangulated surface that uses the Delauny algorithm or a
    similar algorithm complemented with consideration of breaklines, stoplines,
    and maximum length of triangle sides.

    These networks satisfy the Delauny's criterion away from the
    modifications: Fore each triangle in the network, the circle passing
    through its vertices does not contain, in its interior, the vertex
    of any other triangle.

    :ivar stop_lines: Stoplines are lines where the local continuity or
        regularity of the surface is questionable. In the area of these
        pathologies, triangles intersecting a stopline shall be removed
        from the tin surface, leaving holes in the surface. If
        coincidence occurs on surface boundary triangles, the result
        shall be a change of the surface boundary. Stoplines contains
        all these pathological segments as a set of line strings.
    :ivar break_lines: Breaklines are lines of a critical nature to the
        shape of the surface, representing local ridges, or depressions
        (such as drainage lines) in the surface. As such their
        constituent segments must be included in the tin eve if doing so
        violates the Delauny criterion. Break lines contains these
        critical segments as a set of line strings.
    :ivar max_length: Areas of the surface where data is not
        sufficiently dense to assure reasonable calculation shall be
        removed by adding a retention criterion for triangles based on
        the length of their sides. For many triangle sides exceeding
        maximum length, the adjacent triangles to that triangle side
        shall be removed from the surface.
    :ivar control_point: The corners of the triangles in the TIN are
        often referred to as pots. ControlPoint shall contain a set of
        the GM_Position used as posts for this TIN. Since each TIN
        contains triangles, there must be at least 3 posts. The order in
        which these points are given does not affect the surface that is
        represented. Application schemas may add information based on
        ordering of control points to facilitate the reconstruction of
        the TIN from the control points.
    """
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


@dataclass
class TriangulatedSurface(TriangulatedSurfaceType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class Tin(TinType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
