from dataclasses import dataclass
from bindings.csw.vertical_csref_type import VerticalCsrefType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class VerticalCsref(VerticalCsrefType):
    class Meta:
        name = "verticalCSRef"
        namespace = "http://www.opengis.net/gml"
