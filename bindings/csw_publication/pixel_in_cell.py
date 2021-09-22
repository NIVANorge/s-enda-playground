from dataclasses import dataclass
from bindings.csw_publication.pixel_in_cell_type import PixelInCellType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class PixelInCell(PixelInCellType):
    class Meta:
        name = "pixelInCell"
        namespace = "http://www.opengis.net/gml"
