from dataclasses import dataclass
from bindings.wfs.lock_feature_response_type import LockFeatureResponseType

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class LockFeatureResponse(LockFeatureResponseType):
    class Meta:
        namespace = "http://www.opengis.net/wfs/2.0"
