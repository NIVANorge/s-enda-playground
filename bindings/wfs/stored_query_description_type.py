from dataclasses import dataclass, field
from typing import List, Optional
from bindings.wfs.abstract_2 import Abstract2
from bindings.wfs.metadata import Metadata
from bindings.wfs.parameter_expression_type import ParameterExpressionType
from bindings.wfs.query_expression_text_type import QueryExpressionTextType
from bindings.wfs.title_2 import Title2

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class StoredQueryDescriptionType:
    title: List[Title2] = field(
        default_factory=list,
        metadata={
            "name": "Title",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        }
    )
    abstract: List[Abstract2] = field(
        default_factory=list,
        metadata={
            "name": "Abstract",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        }
    )
    metadata: List[Metadata] = field(
        default_factory=list,
        metadata={
            "name": "Metadata",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
        }
    )
    parameter: List[ParameterExpressionType] = field(
        default_factory=list,
        metadata={
            "name": "Parameter",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        }
    )
    query_expression_text: List[QueryExpressionTextType] = field(
        default_factory=list,
        metadata={
            "name": "QueryExpressionText",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
            "min_occurs": 1,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
