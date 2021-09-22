from dataclasses import dataclass, field
from typing import List, Optional
from bindings.csw_publication.element_set_name import ElementSetName
from bindings.csw_publication.request_base_type import RequestBaseType

__NAMESPACE__ = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class GetRecordByIdType(RequestBaseType):
    """Convenience operation to retrieve default record representations by
    identifier.

    Id - object identifier (a URI) that provides a reference to a
    catalogue item (or a result set if the catalogue supports
    persistent result sets).
    ElementSetName - one of "brief, "summary", or "full"
    """
    id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
            "min_occurs": 1,
        }
    )
    element_set_name: Optional[ElementSetName] = field(
        default=None,
        metadata={
            "name": "ElementSetName",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
        }
    )
    output_format: str = field(
        default="application/xml",
        metadata={
            "name": "outputFormat",
            "type": "Attribute",
        }
    )
    output_schema: Optional[str] = field(
        default=None,
        metadata={
            "name": "outputSchema",
            "type": "Attribute",
        }
    )
