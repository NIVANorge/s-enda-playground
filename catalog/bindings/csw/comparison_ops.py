from dataclasses import dataclass
from bindings.csw.comparison_ops_type import ComparisonOpsType

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class ComparisonOps(ComparisonOpsType):
    class Meta:
        name = "comparisonOps"
        namespace = "http://www.opengis.net/ogc"
