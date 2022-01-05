from dataclasses import dataclass
from bindings.csw.abstract_general_operation_parameter_type import AbstractGeneralOperationParameterType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class OperationParameterGroupBaseType(AbstractGeneralOperationParameterType):
    """
    Basic encoding for operation parameter group objects, simplifying and
    restricting the DefinitionType as needed.
    """
