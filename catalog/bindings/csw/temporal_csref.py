from dataclasses import dataclass
from bindings.csw.temporal_csref_type import TemporalCsrefType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TemporalCsref(TemporalCsrefType):
    class Meta:
        name = "temporalCSRef"
        namespace = "http://www.opengis.net/gml"
