from dataclasses import dataclass
from bindings.csw_publication.geometry_style_type import GeometryStyleType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GeometryStyle1(GeometryStyleType):
    """
    The style descriptor for geometries of a feature.
    """
    class Meta:
        name = "GeometryStyle"
        namespace = "http://www.opengis.net/gml"
