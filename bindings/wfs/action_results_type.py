from dataclasses import dataclass, field
from typing import List
from bindings.wfs.created_or_modified_feature_type import CreatedOrModifiedFeatureType

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class ActionResultsType:
    feature: List[CreatedOrModifiedFeatureType] = field(
        default_factory=list,
        metadata={
            "name": "Feature",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
            "min_occurs": 1,
        }
    )
