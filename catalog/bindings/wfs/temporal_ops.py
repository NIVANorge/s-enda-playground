from dataclasses import dataclass
from bindings.wfs.temporal_ops_type import TemporalOpsType

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class TemporalOps(TemporalOpsType):
    class Meta:
        name = "temporalOps"
        namespace = "http://www.opengis.net/fes/2.0"
