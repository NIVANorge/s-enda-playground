from dataclasses import dataclass
from bindings.csw.grid_function_type import GridFunctionType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GridFunction(GridFunctionType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
