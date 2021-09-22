from dataclasses import dataclass
from bindings.csw_publication.line_string_property_type import LineStringPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class LineStringProperty(LineStringPropertyType):
    """Deprecated with GML 3.0 and included only for backwards compatibility
    with GML 2.0.

    Use "curveProperty" instead. This property element either references
    a line string via the XLink-attributes or contains the line string
    element.
    """
    class Meta:
        name = "lineStringProperty"
        namespace = "http://www.opengis.net/gml"
