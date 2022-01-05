from dataclasses import dataclass, field
from bindings.csw.bspline_type import BsplineType
from bindings.csw.curve_interpolation_type import CurveInterpolationType

__NAMESPACE__ = "http://www.opengis.net/gml"


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
