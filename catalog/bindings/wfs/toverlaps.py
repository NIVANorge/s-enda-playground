from dataclasses import dataclass
from bindings.wfs.binary_temporal_op_type import BinaryTemporalOpType

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class Toverlaps(BinaryTemporalOpType):
    class Meta:
        name = "TOverlaps"
        namespace = "http://www.opengis.net/fes/2.0"
