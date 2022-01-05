from dataclasses import dataclass
from bindings.csw.grid_type import GridType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Grid(GridType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
