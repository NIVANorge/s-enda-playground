from dataclasses import dataclass
from bindings.csw_publication.operation_parameter_type import OperationParameterType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class OperationParameter(OperationParameterType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
