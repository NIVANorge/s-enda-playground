from enum import Enum

__NAMESPACE__ = "http://www.opengis.net/gml"


class SuccessionType(Enum):
    SUBSTITUTION = "substitution"
    DIVISION = "division"
    FUSION = "fusion"
    INITIATION = "initiation"
