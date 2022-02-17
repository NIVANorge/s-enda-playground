from dataclasses import dataclass
from bindings.csw.string_or_ref_type import StringOrRefType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Status(StringOrRefType):
    class Meta:
        name = "status"
        namespace = "http://www.opengis.net/gml"
