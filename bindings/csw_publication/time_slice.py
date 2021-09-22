from dataclasses import dataclass
from bindings.csw_publication.abstract_time_slice_type import AbstractTimeSliceType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TimeSlice(AbstractTimeSliceType):
    class Meta:
        name = "_TimeSlice"
        namespace = "http://www.opengis.net/gml"
