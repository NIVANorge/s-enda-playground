from dataclasses import dataclass, field
from typing import Optional
from bindings.gmd.abstract_coverage_type import AbstractCoverageType
from bindings.gmd.coverage_function import CoverageFunction

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractContinuousCoverageType(AbstractCoverageType):
    coverage_function: Optional[CoverageFunction] = field(
        default=None,
        metadata={
            "name": "coverageFunction",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
