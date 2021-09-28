from dataclasses import dataclass, field
from typing import Optional
from bindings.wfs.abstract_adhoc_query_expression_type import AbstractAdhocQueryExpressionType

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class QueryType(AbstractAdhocQueryExpressionType):
    srs_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "srsName",
            "type": "Attribute",
        }
    )
    feature_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "featureVersion",
            "type": "Attribute",
        }
    )
