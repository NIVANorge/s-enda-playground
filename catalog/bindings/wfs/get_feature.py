from dataclasses import dataclass
from bindings.wfs.get_feature_type import GetFeatureType

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class GetFeature(GetFeatureType):
    class Meta:
        namespace = "http://www.opengis.net/wfs/2.0"
