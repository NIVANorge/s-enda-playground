from dataclasses import dataclass
from bindings.csw_publication.category_extent_type import CategoryExtentType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CategoryExtent(CategoryExtentType):
    """Utility element to store a 2-point range of ordinal values.

    If one member is a null, then this is a single ended interval.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml"
