from dataclasses import dataclass
from bindings.gmd.conversion_property_type import ConversionPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ConversionRef(ConversionPropertyType):
    class Meta:
        name = "conversionRef"
        namespace = "http://www.opengis.net/gml"
