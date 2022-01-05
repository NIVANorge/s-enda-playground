from dataclasses import dataclass
from bindings.gmd.bag_type import FeaturePropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class FeatureProperty(FeaturePropertyType):
    class Meta:
        name = "featureProperty"
        namespace = "http://www.opengis.net/gml"
