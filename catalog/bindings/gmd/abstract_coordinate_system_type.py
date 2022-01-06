from dataclasses import dataclass, field
from typing import List, Optional
from bindings.gmd.aggregation_type import AggregationType
from bindings.gmd.axis import Axis
from bindings.gmd.identified_object_type import IdentifiedObjectType
from bindings.gmd.uses_axis import UsesAxis

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractCoordinateSystemType(IdentifiedObjectType):
    uses_axis: List[UsesAxis] = field(
        default_factory=list,
        metadata={
            "name": "usesAxis",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    axis: List[Axis] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    aggregation_type: Optional[AggregationType] = field(
        default=None,
        metadata={
            "name": "aggregationType",
            "type": "Attribute",
        },
    )
