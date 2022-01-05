from dataclasses import dataclass
from bindings.gmd.abstract_geometric_primitive_type import AbstractGeometricPrimitiveType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractGeometricPrimitive(AbstractGeometricPrimitiveType):
    """
    The AbstractGeometricPrimitive element is the abstract head of the
    substitution group for all (pre- and user-defined) geometric primitives.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml"
