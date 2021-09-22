from dataclasses import dataclass
from bindings.csw_publication.operation_parameter_ref_type import OperationParameterRefType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ValueOfParameter(OperationParameterRefType):
    """
    Association to the operation parameter that this is a value of.
    """
    class Meta:
        name = "valueOfParameter"
        namespace = "http://www.opengis.net/gml"
