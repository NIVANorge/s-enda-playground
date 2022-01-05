from dataclasses import dataclass
from bindings.csw.conversion_ref_type import ConversionRefType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ConversionRef(ConversionRefType):
    class Meta:
        name = "conversionRef"
        namespace = "http://www.opengis.net/gml"
