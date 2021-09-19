from dataclasses import dataclass
from bindings.csw.vertical_cstype import VerticalCstype

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class VerticalCs(VerticalCstype):
    class Meta:
        name = "VerticalCS"
        namespace = "http://www.opengis.net/gml"
