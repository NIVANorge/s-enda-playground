from dataclasses import dataclass, field
from typing import Optional
from bindings.csw_publication.abstract_datum_type import AbstractDatumType
from bindings.csw_publication.pixel_in_cell import PixelInCell

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ImageDatumType(AbstractDatumType):
    """An image datum defines the origin of an image coordinate reference
    system, and is used in a local context only.

    For more information, see OGC Abstract Specification Topic 2.
    """
    pixel_in_cell: Optional[PixelInCell] = field(
        default=None,
        metadata={
            "name": "pixelInCell",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
