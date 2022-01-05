from dataclasses import dataclass
from bindings.csw.abstract_parametric_curve_surface_type import AbstractParametricCurveSurfaceType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ParametricCurveSurface(AbstractParametricCurveSurfaceType):
    class Meta:
        name = "_ParametricCurveSurface"
        namespace = "http://www.opengis.net/gml"
