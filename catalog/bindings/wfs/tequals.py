from dataclasses import dataclass
from bindings.wfs.binary_temporal_op_type import BinaryTemporalOpType

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class Tequals(BinaryTemporalOpType):
    class Meta:
        name = "TEquals"
        namespace = "http://www.opengis.net/fes/2.0"
