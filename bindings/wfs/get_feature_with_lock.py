from dataclasses import dataclass
from bindings.wfs.get_feature_with_lock_type import GetFeatureWithLockType

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class GetFeatureWithLock(GetFeatureWithLockType):
    class Meta:
        namespace = "http://www.opengis.net/wfs/2.0"
