from dataclasses import dataclass, field
from typing import List, Optional
from bindings.csw_publication.abstract_style_type import AbstractStyleType
from bindings.csw_publication.feature_style_2 import FeatureStyle2
from bindings.csw_publication.graph_style_2 import GraphStyle2

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class StyleType(AbstractStyleType):
    """[complexType of] Predefined concrete value of the top-level property.

    Encapsulates all other styling information.
    """
    feature_style: List[FeatureStyle2] = field(
        default_factory=list,
        metadata={
            "name": "featureStyle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        }
    )
    graph_style: Optional[GraphStyle2] = field(
        default=None,
        metadata={
            "name": "graphStyle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
