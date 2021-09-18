from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import Optional
from generated.gml.pkg_3.pkg_1.pkg_1.base.basic_types import MeasureType

__NAMESPACE__ = "http://www.opengis.net/gml"


class DegreesTypeValue(Enum):
    N = "N"
    E = "E"
    S = "S"
    W = "W"


@dataclass
class DecimalMinutes:
    class Meta:
        name = "decimalMinutes"
        namespace = "http://www.opengis.net/gml"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": Decimal("0.00"),
            "max_exclusive": Decimal("60.00"),
        }
    )


@dataclass
class Minutes:
    class Meta:
        name = "minutes"
        namespace = "http://www.opengis.net/gml"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
            "max_inclusive": 59,
        }
    )


@dataclass
class Seconds:
    class Meta:
        name = "seconds"
        namespace = "http://www.opengis.net/gml"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": Decimal("0.00"),
            "max_exclusive": Decimal("60.00"),
        }
    )


@dataclass
class AngleType(MeasureType):
    """Value of an angle quantity recorded as a single number, with its units.

    Uses the MeasureType with the restriction that the unit of measure
    referenced by uom must be suitable for an angle, such as degrees or
    radians.
    """


@dataclass
class AreaType(MeasureType):
    """Value of a spatial area quantity, with its units.

    Uses the MeasureType with the restriction that the unit of measure
    referenced by uom must be suitable for an area, such as square
    metres or square miles.
    """


@dataclass
class DegreesType:
    """Integer number of degrees, plus the angle direction.

    This element can be used for geographic Latitude and Longitude. For
    Latitude, the XML attribute direction can take the values "N" or
    "S", meaning North or South of the equator. For Longitude, direction
    can take the values "E" or "W", meaning East or West of the prime
    meridian. This element can also be used for other angles. In that
    case, the direction can take the values "+" or "-" (of SignType), in
    the specified rotational direction from a specified reference
    direction.
    """
    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
            "max_inclusive": 359,
        }
    )
    direction: Optional[DegreesTypeValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class GridLengthType(MeasureType):
    """Value of a length (or distance) quantity in a grid, where the grid
    spacing does not have any associated physical units, or does not have a
    constant physical spacing.

    This grid length will often be used in a digital image grid, where
    the base units are likely to be pixel spacings. Uses the MeasureType
    with the restriction that the unit of measure referenced by uom must
    be suitable for length along the axes of a grid, such as pixel
    spacings or grid spacings.
    """


@dataclass
class LengthType(MeasureType):
    """Value of a length (or distance) quantity, with its units.

    Uses the MeasureType with the restriction that the unit of measure
    referenced by uom must be suitable for a length, such as metres or
    feet.
    """


@dataclass
class ScaleType(MeasureType):
    """Value of a scale factor (or ratio) that has no physical unit.

    Uses the MeasureType with the restriction that the unit of measure
    referenced by uom must be suitable for a scale factor, such as
    percent, permil, or parts-per-million.
    """


@dataclass
class SpeedType(MeasureType):
    """Value of a speed, with its units.

    Uses the MeasureType with the restriction that the unit of measure
    referenced by uom must be suitable for a velocity, such as metres
    per second or miles per hour.
    """


@dataclass
class TimeType(MeasureType):
    """Value of a time or temporal quantity, with its units.

    Uses the MeasureType with the restriction that the unit of measure
    referenced by uom must be suitable for a time value, such as seconds
    or weeks.
    """


@dataclass
class VolumeType(MeasureType):
    """Value of a spatial volume quantity, with its units.

    Uses the MeasureType with the restriction that the unit of measure
    referenced by uom must be suitable for a volume, such as cubic
    metres or cubic feet.
    """


@dataclass
class Angle(MeasureType):
    class Meta:
        name = "angle"
        namespace = "http://www.opengis.net/gml"


@dataclass
class Measure(MeasureType):
    class Meta:
        name = "measure"
        namespace = "http://www.opengis.net/gml"


@dataclass
class Degrees(DegreesType):
    class Meta:
        name = "degrees"
        namespace = "http://www.opengis.net/gml"


@dataclass
class DmsangleType:
    """
    Angle value provided in degree-minute-second or degree-minute format.
    """
    class Meta:
        name = "DMSAngleType"

    degrees: Optional[Degrees] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    decimal_minutes: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "decimalMinutes",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_inclusive": Decimal("0.00"),
            "max_exclusive": Decimal("60.00"),
        }
    )
    minutes: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "max_inclusive": 59,
        }
    )
    seconds: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_inclusive": Decimal("0.00"),
            "max_exclusive": Decimal("60.00"),
        }
    )


@dataclass
class DmsAngle(DmsangleType):
    class Meta:
        name = "dmsAngle"
        namespace = "http://www.opengis.net/gml"


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
