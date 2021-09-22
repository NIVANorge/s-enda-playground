from dataclasses import dataclass
from bindings.csw_publication.concatenated_operation_type import ConcatenatedOperationType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ConcatenatedOperation(ConcatenatedOperationType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
