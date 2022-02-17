from dataclasses import dataclass
from bindings.wfs.range_type import RangeType

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class Range(RangeType):
    class Meta:
        namespace = "http://www.opengis.net/ows/1.1"
