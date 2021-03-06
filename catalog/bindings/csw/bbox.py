from dataclasses import dataclass
from bindings.csw.bboxtype import Bboxtype

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class Bbox(Bboxtype):
    class Meta:
        name = "BBOX"
        namespace = "http://www.opengis.net/ogc"
