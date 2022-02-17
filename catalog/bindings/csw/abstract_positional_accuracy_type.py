from dataclasses import dataclass, field
from typing import Optional
from bindings.csw.measure_description import MeasureDescription

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractPositionalAccuracyType:
    """
    Position error estimate (or accuracy) data.
    """

    measure_description: Optional[MeasureDescription] = field(
        default=None,
        metadata={
            "name": "measureDescription",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
