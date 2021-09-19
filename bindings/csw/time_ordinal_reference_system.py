from dataclasses import dataclass
from bindings.csw.time_ordinal_reference_system_type import TimeOrdinalReferenceSystemType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TimeOrdinalReferenceSystem(TimeOrdinalReferenceSystemType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
