from dataclasses import dataclass, field
from typing import Optional
from bindings.gmd.coverage_mapping_rule import CoverageMappingRule
from bindings.gmd.grid_function import GridFunction
from bindings.gmd.mapping_rule import MappingRule

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CoverageFunctionType:
    mapping_rule: Optional[MappingRule] = field(
        default=None,
        metadata={
            "name": "MappingRule",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    coverage_mapping_rule: Optional[CoverageMappingRule] = field(
        default=None,
        metadata={
            "name": "CoverageMappingRule",
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
