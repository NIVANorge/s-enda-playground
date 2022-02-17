from dataclasses import dataclass
from bindings.gmd.abstract_discrete_coverage_type import AbstractDiscreteCoverageType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MultiCurveCoverageType(AbstractDiscreteCoverageType):
    pass
