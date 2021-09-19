from dataclasses import dataclass, field
from typing import Optional
from bindings.csw.filter import Filter

__NAMESPACE__ = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class QueryConstraintType:
    """A search constraint that adheres to one of the following syntaxes:

    Filter   - OGC filter expression
    CqlText  - OGC CQL predicate

    :ivar filter:
    :ivar cql_text:
    :ivar version: Query language version
    """
    filter: Optional[Filter] = field(
        default=None,
        metadata={
            "name": "Filter",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    cql_text: Optional[str] = field(
        default=None,
        metadata={
            "name": "CqlText",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
        }
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
