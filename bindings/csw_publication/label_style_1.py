from dataclasses import dataclass
from bindings.csw_publication.label_style_type import LabelStyleType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class LabelStyle1(LabelStyleType):
    """
    The style descriptor for labels of a feature, geometry or topology.
    """
    class Meta:
        name = "LabelStyle"
        namespace = "http://www.opengis.net/gml"
