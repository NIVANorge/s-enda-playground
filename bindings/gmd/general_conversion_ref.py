from dataclasses import dataclass
from bindings.gmd.abstract_crstype import GeneralConversionPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GeneralConversionRef(GeneralConversionPropertyType):
    class Meta:
        name = "generalConversionRef"
        namespace = "http://www.opengis.net/gml"
