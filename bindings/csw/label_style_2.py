from dataclasses import dataclass
from bindings.csw.label_style_property_type import LabelStylePropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class LabelStyle2(LabelStylePropertyType):
    class Meta:
        name = "labelStyle"
        namespace = "http://www.opengis.net/gml"
