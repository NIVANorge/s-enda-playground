from dataclasses import dataclass
from bindings.csw_publication.abstract_geometry_type import AbstractGeometryType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractGeometricAggregateType(AbstractGeometryType):
    """
    This is the abstract root type of the geometric aggregates.
    """
