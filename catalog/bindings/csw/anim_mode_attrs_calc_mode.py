from enum import Enum

__NAMESPACE__ = "http://www.w3.org/2001/SMIL20/"


class AnimModeAttrsCalcMode(Enum):
    DISCRETE = "discrete"
    LINEAR = "linear"
    PACED = "paced"
