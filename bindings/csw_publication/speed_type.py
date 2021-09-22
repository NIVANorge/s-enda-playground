from dataclasses import dataclass
from bindings.csw_publication.measure_type import MeasureType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class SpeedType(MeasureType):
    """Value of a speed, with its units.

    Uses the MeasureType with the restriction that the unit of measure
    referenced by uom must be suitable for a velocity, such as metres
    per second or miles per hour.
    """
