from dataclasses import dataclass
from bindings.csw.animate_type import AnimateType

__NAMESPACE__ = "http://www.w3.org/2001/SMIL20/"


@dataclass
class Animate2(AnimateType):
    class Meta:
        name = "animate"
        namespace = "http://www.w3.org/2001/SMIL20/"
