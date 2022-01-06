from dataclasses import dataclass, field
from typing import List
from bindings.wfs.base_request_type import BaseRequestType
from bindings.wfs.stored_query_description_type import StoredQueryDescriptionType

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class CreateStoredQueryType(BaseRequestType):
    stored_query_definition: List[StoredQueryDescriptionType] = field(
        default_factory=list,
        metadata={
            "name": "StoredQueryDefinition",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        },
    )
