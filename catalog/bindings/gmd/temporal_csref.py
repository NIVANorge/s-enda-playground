from dataclasses import dataclass
from bindings.gmd.temporal_csproperty_type import TemporalCspropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TemporalCsref(TemporalCspropertyType):
    class Meta:
        name = "temporalCSRef"
        namespace = "http://www.opengis.net/gml"
