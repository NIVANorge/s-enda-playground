from dataclasses import dataclass
from bindings.csw_publication.logic_ops_type import LogicOpsType

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class LogicOps(LogicOpsType):
    class Meta:
        name = "logicOps"
        namespace = "http://www.opengis.net/ogc"
