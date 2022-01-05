from dataclasses import dataclass
from bindings.csw.abstract_coordinate_system_type import AbstractCoordinateSystemType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ObliqueCartesianCstype(AbstractCoordinateSystemType):
    """A two- or three-dimensional coordinate system with straight axes that
    are not necessarily orthogonal.

    An ObliqueCartesianCS shall have two or three usesAxis associations.
    """
    class Meta:
        name = "ObliqueCartesianCSType"
