from dataclasses import dataclass, field
from typing import List
from bindings.wfs.feature_type_type import FeatureTypeType

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class FeatureTypeListType:
    feature_type: List[FeatureTypeType] = field(
        default_factory=list,
        metadata={
            "name": "FeatureType",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
            "min_occurs": 1,
        },
    )
