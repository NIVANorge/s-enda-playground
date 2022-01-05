from dataclasses import dataclass
from bindings.ows.range_type import RangeType

__NAMESPACE__ = "http://www.opengis.net/ows/2.0"


@dataclass
class Range(RangeType):
    class Meta:
        namespace = "http://www.opengis.net/ows/2.0"
