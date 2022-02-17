from dataclasses import dataclass
from bindings.csw.graph_style_type import GraphStyleType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GraphStyle1(GraphStyleType):
    """The style descriptor for a graph consisting of a number of features.

    Describes graph-specific style attributes.
    """

    class Meta:
        name = "GraphStyle"
        namespace = "http://www.opengis.net/gml"
