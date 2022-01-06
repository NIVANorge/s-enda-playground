from dataclasses import dataclass, field
from typing import List
from bindings.csw.abstract_time_reference_system_type import (
    AbstractTimeReferenceSystemType,
)
from bindings.csw.time_ordinal_era_type import TimeOrdinalEraPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TimeOrdinalReferenceSystemType(AbstractTimeReferenceSystemType):
    """
    In an ordinal reference system the order of events in time can be well
    established, but the magnitude of the intervals between them can not be
    accurately determined (e.g. a stratigraphic sequence).
    """

    component: List[TimeOrdinalEraPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        },
    )
