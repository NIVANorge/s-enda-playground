from dataclasses import dataclass
from bindings.csw.arc_type_1 import ArcType1

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Arc1(ArcType1):
    class Meta:
        name = "Arc"
        namespace = "http://www.opengis.net/gml"
