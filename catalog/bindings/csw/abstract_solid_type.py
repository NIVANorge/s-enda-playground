from dataclasses import dataclass
from bindings.csw.abstract_geometric_primitive_type import (
    AbstractGeometricPrimitiveType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractSolidType(AbstractGeometricPrimitiveType):
    """An abstraction of a solid to support the different levels of complexity.

    A solid is always contiguous.
    """
