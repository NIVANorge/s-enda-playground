from dataclasses import dataclass
from bindings.csw.image_crsref_type import ImageCrsrefType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ImageCrsref(ImageCrsrefType):
    class Meta:
        name = "imageCRSRef"
        namespace = "http://www.opengis.net/gml"
