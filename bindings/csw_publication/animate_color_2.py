from dataclasses import dataclass
from bindings.csw_publication.animate_color_type import AnimateColorType

__NAMESPACE__ = "http://www.w3.org/2001/SMIL20/"


@dataclass
class AnimateColor2(AnimateColorType):
    class Meta:
        name = "animateColor"
        namespace = "http://www.w3.org/2001/SMIL20/"
