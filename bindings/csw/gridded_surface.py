from dataclasses import dataclass
from bindings.csw.abstract_gridded_surface_type import AbstractGriddedSurfaceType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GriddedSurface(AbstractGriddedSurfaceType):
    class Meta:
        name = "_GriddedSurface"
        namespace = "http://www.opengis.net/gml"
