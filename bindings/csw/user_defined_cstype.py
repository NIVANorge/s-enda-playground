from dataclasses import dataclass
from bindings.csw.abstract_coordinate_system_type import AbstractCoordinateSystemType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class UserDefinedCstype(AbstractCoordinateSystemType):
    """A two- or three-dimensional coordinate system that consists of any
    combination of coordinate axes not covered by any other coordinate system
    type.

    An example is a multilinear coordinate system which contains one
    coordinate axis that may have any 1-D shape which has no
    intersections with itself. This non-straight axis is supplemented by
    one or two straight axes to complete a 2 or 3 dimensional coordinate
    system. The non-straight axis is typically incrementally straight or
    curved. A UserDefinedCS shall have two or three usesAxis
    associations.
    """
    class Meta:
        name = "UserDefinedCSType"
