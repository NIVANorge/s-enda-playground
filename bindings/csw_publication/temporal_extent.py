from dataclasses import dataclass
from bindings.csw_publication.abstract_time_primitive_type import TimePeriodType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TemporalExtent(TimePeriodType):
    """
    A time period defining the temporal domain of this object.
    """
    class Meta:
        name = "temporalExtent"
        namespace = "http://www.opengis.net/gml"
