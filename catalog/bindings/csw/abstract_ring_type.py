from dataclasses import dataclass
from bindings.csw.abstract_geometry_type import AbstractGeometryType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractRingType(AbstractGeometryType):
    """
    An abstraction of a ring to support surface boundaries of different
    complexity.
    """
