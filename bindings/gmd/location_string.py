from dataclasses import dataclass
from bindings.gmd.string_or_ref_type import StringOrRefType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class LocationString(StringOrRefType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
