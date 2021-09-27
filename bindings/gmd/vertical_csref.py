from dataclasses import dataclass
from bindings.gmd.vertical_csproperty_type import VerticalCspropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class VerticalCsref(VerticalCspropertyType):
    class Meta:
        name = "verticalCSRef"
        namespace = "http://www.opengis.net/gml"
