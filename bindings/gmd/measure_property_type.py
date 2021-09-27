from dataclasses import dataclass, field
from typing import Optional, Union
from bindings.gmd.angle_1 import Angle1
from bindings.gmd.distance import Distance
from bindings.gmd.length import Length
from bindings.gmd.measure_1 import Measure1
from bindings.gmd.nil_reason_enumeration_value import NilReasonEnumerationValue
from bindings.gmd.scale import Scale

__NAMESPACE__ = "http://www.isotc211.org/2005/gco"


@dataclass
class MeasurePropertyType:
    class Meta:
        name = "Measure_PropertyType"

    scale: Optional[Scale] = field(
        default=None,
        metadata={
            "name": "Scale",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gco",
        }
    )
    angle: Optional[Angle1] = field(
        default=None,
        metadata={
            "name": "Angle",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gco",
        }
    )
    distance: Optional[Distance] = field(
        default=None,
        metadata={
            "name": "Distance",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gco",
        }
    )
    length: Optional[Length] = field(
        default=None,
        metadata={
            "name": "Length",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gco",
        }
    )
    measure: Optional[Measure1] = field(
        default=None,
        metadata={
            "name": "Measure",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gco",
        }
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "namespace": "http://www.isotc211.org/2005/gco",
            "pattern": r"other:\w{2,}",
        }
    )
