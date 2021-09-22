from dataclasses import dataclass, field
from typing import List
from bindings.csw_publication.schema_component_type import SchemaComponentType

__NAMESPACE__ = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class DescribeRecordResponseType:
    """
    The response contains a list of matching schema components in the requested
    schema language.
    """
    schema_component: List[SchemaComponentType] = field(
        default_factory=list,
        metadata={
            "name": "SchemaComponent",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
        }
    )
