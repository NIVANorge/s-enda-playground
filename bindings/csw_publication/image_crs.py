from dataclasses import dataclass
from bindings.csw_publication.image_crstype import ImageCrstype

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ImageCrs(ImageCrstype):
    class Meta:
        name = "ImageCRS"
        namespace = "http://www.opengis.net/gml"
