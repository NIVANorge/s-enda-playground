from dataclasses import dataclass
from bindings.gmd.abstract_general_operation_parameter_type import (
    AbstractGeneralOperationParameterType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractGeneralOperationParameter(AbstractGeneralOperationParameterType):
    """
    gml:GeneralOperationParameter is the abstract definition of a parameter or
    group of parameters used by an operation method.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml"
