from dataclasses import dataclass
from bindings.csw_publication.measure_type import MeasureType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class SemiMajorAxis(MeasureType):
    """Length of the semi-major axis of the ellipsoid, with its units.

    Uses the MeasureType with the restriction that the unit of measure
    referenced by uom must be suitable for a length, such as metres or
    feet.
    """
    class Meta:
        name = "semiMajorAxis"
        namespace = "http://www.opengis.net/gml"
