from dataclasses import dataclass
from bindings.csw.abstract_general_operation_parameter_type import (
    AbstractGeneralOperationParameterType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GeneralOperationParameter(AbstractGeneralOperationParameterType):
    class Meta:
        name = "_GeneralOperationParameter"
        namespace = "http://www.opengis.net/gml"
