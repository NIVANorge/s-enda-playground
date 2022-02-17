from dataclasses import dataclass
from bindings.csw.general_conversion_ref_type import GeneralConversionRefType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GeneralConversionRef(GeneralConversionRefType):
    class Meta:
        name = "generalConversionRef"
        namespace = "http://www.opengis.net/gml"
