from dataclasses import dataclass, field
from typing import Optional
from bindings.csw.abstract_reference_system_type import AbstractReferenceSystemType
from bindings.csw.uses_temporal_cs import UsesTemporalCs
from bindings.csw.uses_temporal_datum import UsesTemporalDatum

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TemporalCrstype(AbstractReferenceSystemType):
    """
    A 1D coordinate reference system used for the recording of time.
    """
    class Meta:
        name = "TemporalCRSType"

    uses_temporal_cs: Optional[UsesTemporalCs] = field(
        default=None,
        metadata={
            "name": "usesTemporalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    uses_temporal_datum: Optional[UsesTemporalDatum] = field(
        default=None,
        metadata={
            "name": "usesTemporalDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
