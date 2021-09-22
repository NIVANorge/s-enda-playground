from dataclasses import dataclass
from bindings.csw_publication.temporal_crsref_type import TemporalCrsrefType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TemporalCrsref(TemporalCrsrefType):
    class Meta:
        name = "temporalCRSRef"
        namespace = "http://www.opengis.net/gml"
