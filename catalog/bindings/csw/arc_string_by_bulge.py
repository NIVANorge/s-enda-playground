from dataclasses import dataclass
from bindings.csw.arc_string_by_bulge_type import ArcStringByBulgeType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ArcStringByBulge(ArcStringByBulgeType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
