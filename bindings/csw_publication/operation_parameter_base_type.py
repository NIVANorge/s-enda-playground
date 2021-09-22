from dataclasses import dataclass
from bindings.csw_publication.abstract_general_operation_parameter_type import AbstractGeneralOperationParameterType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class OperationParameterBaseType(AbstractGeneralOperationParameterType):
    """
    Basic encoding for operation parameter objects, simplifying and restricting
    the DefinitionType as needed.
    """
