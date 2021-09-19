from dataclasses import dataclass
from bindings.csw.code_type_2 import CodeType2

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class PixelInCellType(CodeType2):
    """
    Specification of the way an image grid is associated with the image data
    attributes.
    """
