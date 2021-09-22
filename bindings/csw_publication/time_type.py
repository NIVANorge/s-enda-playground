from dataclasses import dataclass
from bindings.csw_publication.measure_type import MeasureType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TimeType(MeasureType):
    """Value of a time or temporal quantity, with its units.

    Uses the MeasureType with the restriction that the unit of measure
    referenced by uom must be suitable for a time value, such as seconds
    or weeks.
    """
