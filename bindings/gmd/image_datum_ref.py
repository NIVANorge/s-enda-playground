from dataclasses import dataclass
from bindings.gmd.abstract_crstype import ImageDatumPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ImageDatumRef(ImageDatumPropertyType):
    class Meta:
        name = "imageDatumRef"
        namespace = "http://www.opengis.net/gml"
