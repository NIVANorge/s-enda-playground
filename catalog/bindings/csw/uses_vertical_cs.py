from dataclasses import dataclass
from bindings.csw.vertical_csref_type import VerticalCsrefType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class UsesVerticalCs(VerticalCsrefType):
    """
    Association to the vertical coordinate system used by this CRS.
    """
    class Meta:
        name = "usesVerticalCS"
        namespace = "http://www.opengis.net/gml"
