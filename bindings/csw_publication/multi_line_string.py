from dataclasses import dataclass
from bindings.csw_publication.multi_line_string_type import MultiLineStringType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MultiLineString(MultiLineStringType):
    """Deprecated with GML 3.0 and included for backwards compatibility with
    GML 2.

    Use the "MultiCurve" element instead.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml"
