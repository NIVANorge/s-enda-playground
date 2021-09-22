from dataclasses import dataclass
from bindings.csw_publication.extent_type import ExtentType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ValidArea(ExtentType):
    """
    Area or region in which this CRS object is valid.
    """
    class Meta:
        name = "validArea"
        namespace = "http://www.opengis.net/gml"
