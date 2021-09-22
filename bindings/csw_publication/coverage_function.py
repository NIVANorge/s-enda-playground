from dataclasses import dataclass
from bindings.csw_publication.coverage_function_type import CoverageFunctionType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CoverageFunction(CoverageFunctionType):
    class Meta:
        name = "coverageFunction"
        namespace = "http://www.opengis.net/gml"
