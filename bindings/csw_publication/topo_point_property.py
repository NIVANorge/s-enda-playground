from dataclasses import dataclass
from bindings.csw_publication.topo_point_property_type import TopoPointPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TopoPointProperty(TopoPointPropertyType):
    class Meta:
        name = "topoPointProperty"
        namespace = "http://www.opengis.net/gml"
