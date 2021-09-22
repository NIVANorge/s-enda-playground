from dataclasses import dataclass
from bindings.csw_publication.abstract_ring_property_type import AbstractRingPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class OuterBoundaryIs(AbstractRingPropertyType):
    """Deprecated with GML 3.0, included only for backwards compatibility with
    GML 2.

    Use "exterior" instead.
    """
    class Meta:
        name = "outerBoundaryIs"
        namespace = "http://www.opengis.net/gml"
