from dataclasses import dataclass, field
from typing import Optional
from bindings.csw.grid_function import GridFunction
from bindings.csw.index_map import IndexMap
from bindings.csw.mapping_rule import MappingRule

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CoverageFunctionType:
    """The function or rule which defines the map from members of the domainSet
    to the range.

    More functions will be added to this list
    """
    mapping_rule: Optional[MappingRule] = field(
        default=None,
        metadata={
            "name": "MappingRule",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    index_map: Optional[IndexMap] = field(
        default=None,
        metadata={
            "name": "IndexMap",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    grid_function: Optional[GridFunction] = field(
        default=None,
        metadata={
            "name": "GridFunction",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
