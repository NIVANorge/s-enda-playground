from dataclasses import dataclass
from bindings.csw_publication.arc_type_2 import ArcType2

__NAMESPACE__ = "http://www.w3.org/1999/xlink"


@dataclass
class Arc2(ArcType2):
    class Meta:
        name = "arc"
        namespace = "http://www.w3.org/1999/xlink"
