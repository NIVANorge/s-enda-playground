from dataclasses import dataclass
from bindings.csw_publication.operation_method_type import OperationMethodType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class OperationMethod(OperationMethodType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
