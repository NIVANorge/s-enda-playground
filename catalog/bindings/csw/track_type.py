from dataclasses import dataclass
from bindings.csw.history_property_type import HistoryPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TrackType(HistoryPropertyType):
    """
    The track of a moving object is a sequence of specialized timeslices
    that indicate the status of the object.
    """
