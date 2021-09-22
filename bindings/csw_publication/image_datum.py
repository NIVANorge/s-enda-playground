from dataclasses import dataclass
from bindings.csw_publication.image_datum_type import ImageDatumType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ImageDatum(ImageDatumType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
