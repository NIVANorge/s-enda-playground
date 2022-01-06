from dataclasses import dataclass, field
from typing import List, Optional
from bindings.csw.abstract_curve_segment_type import AbstractCurveSegmentType
from bindings.csw.coordinates import Coordinates
from bindings.csw.curve_interpolation_type import CurveInterpolationType
from bindings.csw.knot_property_type import KnotPropertyType
from bindings.csw.knot_types_type import KnotTypesType
from bindings.csw.point_property import PointProperty
from bindings.csw.point_rep import PointRep
from bindings.csw.pos import Pos
from bindings.csw.pos_list import PosList

__NAMESPACE__ = "http://www.opengis.net/gml"


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
        },
    )
    point_property: List[PointProperty] = field(
        default_factory=list,
        metadata={
            "name": "pointProperty",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        },
    )
    point_rep: List[PointRep] = field(
        default_factory=list,
        metadata={
            "name": "pointRep",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        },
    )
    pos_list: Optional[PosList] = field(
        default=None,
        metadata={
            "name": "posList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    coordinates: Optional[Coordinates] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    degree: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    knot: List[KnotPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 2,
        },
    )
    interpolation: CurveInterpolationType = field(
        default=CurveInterpolationType.POLYNOMIAL_SPLINE,
        metadata={
            "type": "Attribute",
        },
    )
    is_polynomial: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isPolynomial",
            "type": "Attribute",
        },
    )
    knot_type: Optional[KnotTypesType] = field(
        default=None,
        metadata={
            "name": "knotType",
            "type": "Attribute",
        },
    )
