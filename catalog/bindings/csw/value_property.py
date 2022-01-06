from dataclasses import dataclass
from bindings.csw.feature_array_property_type import ValuePropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ValueProperty(ValuePropertyType):
    """
    Element which refers to, or contains, a Value.
    """

    class Meta:
        name = "valueProperty"
        namespace = "http://www.opengis.net/gml"
