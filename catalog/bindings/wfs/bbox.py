from dataclasses import dataclass
from bindings.wfs.bboxtype import Bboxtype

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class Bbox(Bboxtype):
    class Meta:
        name = "BBOX"
        namespace = "http://www.opengis.net/fes/2.0"
