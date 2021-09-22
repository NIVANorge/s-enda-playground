from dataclasses import dataclass
from bindings.csw_publication.abstract_surface_patch_type import AbstractSurfacePatchType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractParametricCurveSurfaceType(AbstractSurfacePatchType):
    pass
