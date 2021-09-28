from dataclasses import dataclass
from bindings.wfs.lock_feature_type import LockFeatureType

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class LockFeature(LockFeatureType):
    class Meta:
        namespace = "http://www.opengis.net/wfs/2.0"
