from dataclasses import dataclass
from bindings.csw.container_property_type import AbstractTopoPrimitiveType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TopoPrimitive(AbstractTopoPrimitiveType):
    """
    Substitution group branch for Topo Primitives, used by
    TopoPrimitiveArrayAssociationType.
    """

    class Meta:
        name = "_TopoPrimitive"
        namespace = "http://www.opengis.net/gml"
