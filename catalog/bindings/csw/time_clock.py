from dataclasses import dataclass
from bindings.csw.time_clock_type import TimeClockType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TimeClock(TimeClockType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
