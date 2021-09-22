from dataclasses import dataclass
from bindings.csw_publication.graph_style_property_type import GraphStylePropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GraphStyle2(GraphStylePropertyType):
    class Meta:
        name = "graphStyle"
        namespace = "http://www.opengis.net/gml"
