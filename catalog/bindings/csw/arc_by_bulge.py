from dataclasses import dataclass
from bindings.csw.arc_by_bulge_type import ArcByBulgeType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ArcByBulge(ArcByBulgeType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
