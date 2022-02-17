from dataclasses import dataclass
from bindings.csw.style_type import StyleType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Style1(StyleType):
    """Predefined concrete value of the top-level property.

    Encapsulates all other styling information.
    """

    class Meta:
        name = "Style"
        namespace = "http://www.opengis.net/gml"
