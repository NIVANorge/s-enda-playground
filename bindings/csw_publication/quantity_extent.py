from dataclasses import dataclass
from bindings.csw_publication.quantity_extent_type import QuantityExtentType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class QuantityExtent(QuantityExtentType):
    """Utility element to store a 2-point range of numeric values.

    If one member is a null, then this is a single ended interval.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml"
