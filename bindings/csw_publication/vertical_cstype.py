from dataclasses import dataclass
from bindings.csw_publication.abstract_coordinate_system_type import AbstractCoordinateSystemType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class VerticalCstype(AbstractCoordinateSystemType):
    """A one-dimensional coordinate system used to record the heights (or
    depths) of points.

    Such a coordinate system is usually dependent on the Earth's gravity
    field, perhaps loosely as when atmospheric pressure is the basis for
    the vertical coordinate system axis. A VerticalCS shall have one
    usesAxis association.
    """
    class Meta:
        name = "VerticalCSType"
