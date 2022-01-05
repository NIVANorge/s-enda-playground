from dataclasses import dataclass
from bindings.csw.image_datum_ref_type import ImageDatumRefType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ImageDatumRef(ImageDatumRefType):
    class Meta:
        name = "imageDatumRef"
        namespace = "http://www.opengis.net/gml"
