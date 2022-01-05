from dataclasses import dataclass
from bindings.gmd.image_crsproperty_type import ImageCrspropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ImageCrsref(ImageCrspropertyType):
    class Meta:
        name = "imageCRSRef"
        namespace = "http://www.opengis.net/gml"
