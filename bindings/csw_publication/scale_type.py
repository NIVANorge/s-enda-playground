from dataclasses import dataclass
from bindings.csw_publication.measure_type import MeasureType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ScaleType(MeasureType):
    """Value of a scale factor (or ratio) that has no physical unit.

    Uses the MeasureType with the restriction that the unit of measure
    referenced by uom must be suitable for a scale factor, such as
    percent, permil, or parts-per-million.
    """
