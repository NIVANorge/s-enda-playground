from dataclasses import dataclass, field
from typing import List, Optional
from xml.etree.ElementTree import QName
from bindings.csw.abstract_query_type import AbstractQueryType
from bindings.csw.constraint import Constraint
from bindings.csw.element_set_name import ElementSetName
from bindings.csw.sort_by import SortBy

__NAMESPACE__ = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class QueryType(AbstractQueryType):
    """Specifies a query to execute against instances of one or more object
    types. A set of ElementName elements may be included to specify an adhoc
    view of the csw:Record instances in the result set. Otherwise, use
    ElementSetName to specify a predefined view. The Constraint element
    contains a query filter expressed in a supported query language. A sorting
    criterion that specifies a property to sort by may be included.

    typeNames - a list of object types to query.
    """

    element_set_name: Optional[ElementSetName] = field(
        default=None,
        metadata={
            "name": "ElementSetName",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
        },
    )
    element_name: List[QName] = field(
        default_factory=list,
        metadata={
            "name": "ElementName",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
        },
    )
    constraint: Optional[Constraint] = field(
        default=None,
        metadata={
            "name": "Constraint",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
        },
    )
    sort_by: Optional[SortBy] = field(
        default=None,
        metadata={
            "name": "SortBy",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    type_names: List[QName] = field(
        default_factory=list,
        metadata={
            "name": "typeNames",
            "type": "Attribute",
            "required": True,
            "tokens": True,
        },
    )
