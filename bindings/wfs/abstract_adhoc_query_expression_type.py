from dataclasses import dataclass, field
from typing import List, Optional
from bindings.wfs.abstract_projection_clause import AbstractProjectionClause
from bindings.wfs.abstract_query_expression_type import AbstractQueryExpressionType
from bindings.wfs.abstract_selection_clause import AbstractSelectionClause
from bindings.wfs.abstract_sorting_clause import AbstractSortingClause
from bindings.wfs.filter import Filter
from bindings.wfs.property_name import PropertyName
from bindings.wfs.sort_by import SortBy

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class AbstractAdhocQueryExpressionType(AbstractQueryExpressionType):
    property_name: List[PropertyName] = field(
        default_factory=list,
        metadata={
            "name": "PropertyName",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        }
    )
    abstract_projection_clause: List[AbstractProjectionClause] = field(
        default_factory=list,
        metadata={
            "name": "AbstractProjectionClause",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        }
    )
    filter: Optional[Filter] = field(
        default=None,
        metadata={
            "name": "Filter",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        }
    )
    abstract_selection_clause: Optional[AbstractSelectionClause] = field(
        default=None,
        metadata={
            "name": "AbstractSelectionClause",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        }
    )
    sort_by: Optional[SortBy] = field(
        default=None,
        metadata={
            "name": "SortBy",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        }
    )
    abstract_sorting_clause: Optional[AbstractSortingClause] = field(
        default=None,
        metadata={
            "name": "AbstractSortingClause",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        }
    )
    type_names: List[str] = field(
        default_factory=list,
        metadata={
            "name": "typeNames",
            "type": "Attribute",
            "required": True,
            "pattern": r"schema\-element\(.+\)",
            "tokens": True,
        }
    )
    aliases: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
