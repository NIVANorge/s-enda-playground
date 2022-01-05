from dataclasses import dataclass
from bindings.gmd.temporal_crsproperty_type import TemporalCrspropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TemporalCrsref(TemporalCrspropertyType):
    class Meta:
        name = "temporalCRSRef"
        namespace = "http://www.opengis.net/gml"
