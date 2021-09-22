from dataclasses import dataclass
from bindings.csw_publication.bezier_type import BezierType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Bezier(BezierType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
