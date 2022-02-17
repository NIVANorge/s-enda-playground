from dataclasses import dataclass, field
from typing import Optional
from bindings.csw.envelope import Envelope
from bindings.csw.envelope_with_time_period import EnvelopeWithTimePeriod
from bindings.csw.property_name import PropertyName
from bindings.csw.spatial_ops_type import SpatialOpsType

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class Bboxtype(SpatialOpsType):
    class Meta:
        name = "BBOXType"

    property_name: Optional[PropertyName] = field(
        default=None,
        metadata={
            "name": "PropertyName",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    envelope_with_time_period: Optional[EnvelopeWithTimePeriod] = field(
        default=None,
        metadata={
            "name": "EnvelopeWithTimePeriod",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    envelope: Optional[Envelope] = field(
        default=None,
        metadata={
            "name": "Envelope",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
