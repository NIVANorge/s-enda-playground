from dataclasses import dataclass, field
from typing import List, Optional
from bindings.csw_publication.aeshetic_criteria_type import AesheticCriteriaType
from bindings.csw_publication.base_style_descriptor_type import BaseStyleDescriptorType
from bindings.csw_publication.drawing_type_type import DrawingTypeType
from bindings.csw_publication.graph_type_type import GraphTypeType
from bindings.csw_publication.line_type_type import LineTypeType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GraphStyleType(BaseStyleDescriptorType):
    """[complexType of] The style descriptor for a graph consisting of a number
    of features.

    Describes graph-specific style attributes.
    """
    planar: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    directed: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    grid: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    min_distance: Optional[float] = field(
        default=None,
        metadata={
            "name": "minDistance",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    min_angle: Optional[float] = field(
        default=None,
        metadata={
            "name": "minAngle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    graph_type: Optional[GraphTypeType] = field(
        default=None,
        metadata={
            "name": "graphType",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    drawing_type: Optional[DrawingTypeType] = field(
        default=None,
        metadata={
            "name": "drawingType",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    line_type: Optional[LineTypeType] = field(
        default=None,
        metadata={
            "name": "lineType",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    aesthetic_criteria: List[AesheticCriteriaType] = field(
        default_factory=list,
        metadata={
            "name": "aestheticCriteria",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
