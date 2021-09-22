from dataclasses import dataclass
from bindings.csw_publication.time_calendar_type import TimeCalendarType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TimeCalendar(TimeCalendarType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
