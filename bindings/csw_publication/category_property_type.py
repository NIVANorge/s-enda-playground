from dataclasses import dataclass
from bindings.csw_publication.feature_array_property_type import ValuePropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CategoryPropertyType(ValuePropertyType):
    """
    Property whose content is a Category.
    """
