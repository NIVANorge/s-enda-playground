from dataclasses import dataclass
from bindings.csw.pass_through_operation_type import PassThroughOperationType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class PassThroughOperation(PassThroughOperationType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
