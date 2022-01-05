from dataclasses import dataclass, field
from typing import Optional
from bindings.wfs.features_locked_type import FeaturesLockedType
from bindings.wfs.features_not_locked_type import FeaturesNotLockedType

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class LockFeatureResponseType:
    features_locked: Optional[FeaturesLockedType] = field(
        default=None,
        metadata={
            "name": "FeaturesLocked",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        }
    )
    features_not_locked: Optional[FeaturesNotLockedType] = field(
        default=None,
        metadata={
            "name": "FeaturesNotLocked",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        }
    )
    lock_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "lockId",
            "type": "Attribute",
        }
    )
