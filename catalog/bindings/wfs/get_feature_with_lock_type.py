from dataclasses import dataclass, field
from bindings.wfs.all_some_type import AllSomeType
from bindings.wfs.get_feature_type import GetFeatureType

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class GetFeatureWithLockType(GetFeatureType):
    expiry: int = field(
        default=300,
        metadata={
            "type": "Attribute",
        },
    )
    lock_action: AllSomeType = field(
        default=AllSomeType.ALL,
        metadata={
            "name": "lockAction",
            "type": "Attribute",
        },
    )
