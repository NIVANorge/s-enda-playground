from dataclasses import dataclass, field
from typing import List, Optional
from bindings.csw.abstract_geometry_type import AbstractGeometryType
from bindings.csw.grid_limits_type import GridLimitsType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GridType(AbstractGeometryType):
    """
    An unrectified grid, which is a network composed of two or more sets of
    equally spaced parallel lines in which the members of each set intersect
    the members of the other sets at right angles.
    """
    limits: Optional[GridLimitsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    axis_name: List[str] = field(
        default_factory=list,
        metadata={
            "name": "axisName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        }
    )
    dimension: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
