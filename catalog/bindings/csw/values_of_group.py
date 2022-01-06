from dataclasses import dataclass
from bindings.csw.operation_parameter_group_ref_type import (
    OperationParameterGroupRefType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ValuesOfGroup(OperationParameterGroupRefType):
    """
    Association to the operation parameter group for which this element
    provides parameter values.
    """

    class Meta:
        name = "valuesOfGroup"
        namespace = "http://www.opengis.net/gml"
