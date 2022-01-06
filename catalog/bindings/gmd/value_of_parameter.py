from dataclasses import dataclass
from bindings.gmd.operation_parameter_property_type import (
    OperationParameterPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ValueOfParameter(OperationParameterPropertyType):
    class Meta:
        name = "valueOfParameter"
        namespace = "http://www.opengis.net/gml"
