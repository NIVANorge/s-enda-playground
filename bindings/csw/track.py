from dataclasses import dataclass
from bindings.csw.track_type import TrackType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Track(TrackType):
    class Meta:
        name = "track"
        namespace = "http://www.opengis.net/gml"
