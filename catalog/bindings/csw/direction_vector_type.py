from dataclasses import dataclass, field
from typing import Optional
from bindings.csw.angle_type import AngleType
from bindings.csw.vector import Vector

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DirectionVectorType:
    """
    Direction expressed as a vector, either using components, or using angles.
    """
    vector: Optional[Vector] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    horizontal_angle: Optional[AngleType] = field(
        default=None,
        metadata={
            "name": "horizontalAngle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    vertical_angle: Optional[AngleType] = field(
        default=None,
        metadata={
            "name": "verticalAngle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
