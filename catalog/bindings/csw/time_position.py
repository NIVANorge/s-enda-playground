from dataclasses import dataclass
from bindings.csw.time_position_type import TimePositionType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TimePosition(TimePositionType):
    """
    Direct representation of a temporal position.
    """

    class Meta:
        name = "timePosition"
        namespace = "http://www.opengis.net/gml"
