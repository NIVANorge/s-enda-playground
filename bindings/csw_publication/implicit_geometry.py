from dataclasses import dataclass
from bindings.csw_publication.abstract_geometry_type import AbstractGeometryType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ImplicitGeometry(AbstractGeometryType):
    class Meta:
        name = "_ImplicitGeometry"
        namespace = "http://www.opengis.net/gml"
