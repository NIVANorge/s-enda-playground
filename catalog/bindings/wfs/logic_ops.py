from dataclasses import dataclass
from bindings.wfs.logic_ops_type import LogicOpsType

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class LogicOps(LogicOpsType):
    class Meta:
        name = "logicOps"
        namespace = "http://www.opengis.net/fes/2.0"
