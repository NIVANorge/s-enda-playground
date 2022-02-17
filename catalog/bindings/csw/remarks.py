from dataclasses import dataclass
from bindings.csw.string_or_ref_type import StringOrRefType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Remarks(StringOrRefType):
    """Information about this object or code.

    Contains text or refers to external text.
    """

    class Meta:
        name = "remarks"
        namespace = "http://www.opengis.net/gml"
