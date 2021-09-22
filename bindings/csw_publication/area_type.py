from dataclasses import dataclass
from bindings.csw_publication.measure_type import MeasureType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AreaType(MeasureType):
    """Value of a spatial area quantity, with its units.

    Uses the MeasureType with the restriction that the unit of measure
    referenced by uom must be suitable for an area, such as square
    metres or square miles.
    """
