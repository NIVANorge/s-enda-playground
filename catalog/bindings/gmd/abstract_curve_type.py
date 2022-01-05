from dataclasses import dataclass
from bindings.gmd.abstract_geometric_primitive_type import AbstractGeometricPrimitiveType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractCurveType(AbstractGeometricPrimitiveType):
    """gml:AbstractCurveType is an abstraction of a curve to support the
    different levels of complexity.

    The curve may always be viewed as a geometric primitive, i.e. is
    continuous.
    """
