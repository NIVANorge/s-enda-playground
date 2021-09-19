from dataclasses import dataclass
from bindings.csw.abstract_surface_type import AbstractSurfaceType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Surface2(AbstractSurfaceType):
    """
    The "_Surface" element is the abstract head of the substituition group for
    all (continuous) surface elements.
    """
    class Meta:
        name = "_Surface"
        namespace = "http://www.opengis.net/gml"
