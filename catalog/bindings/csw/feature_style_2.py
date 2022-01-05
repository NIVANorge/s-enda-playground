from dataclasses import dataclass
from bindings.csw.feature_style_property_type import FeatureStylePropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class FeatureStyle2(FeatureStylePropertyType):
    class Meta:
        name = "featureStyle"
        namespace = "http://www.opengis.net/gml"
