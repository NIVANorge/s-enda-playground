from dataclasses import dataclass
from bindings.csw.feature_style_type import FeatureStyleType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class FeatureStyle1(FeatureStyleType):
    """
    The style descriptor for features.
    """

    class Meta:
        name = "FeatureStyle"
        namespace = "http://www.opengis.net/gml"
