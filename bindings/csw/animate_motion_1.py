from dataclasses import dataclass
from bindings.csw.animate_motion_type import AnimateMotionType

__NAMESPACE__ = "http://www.w3.org/2001/SMIL20/Language"


@dataclass
class AnimateMotion1(AnimateMotionType):
    class Meta:
        name = "animateMotion"
        namespace = "http://www.w3.org/2001/SMIL20/Language"
