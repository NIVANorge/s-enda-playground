from dataclasses import dataclass, field
from typing import Optional
from bindings.csw_publication.angle import Angle
from bindings.csw_publication.dms_angle import DmsAngle

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AngleChoiceType:
    """
    Value of an angle quantity provided in either degree-minute-second format
    or single value format.
    """
    angle: Optional[Angle] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    dms_angle: Optional[DmsAngle] = field(
        default=None,
        metadata={
            "name": "dmsAngle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
