from dataclasses import dataclass
from bindings.csw.parameter_value_type import ParameterValueType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ParameterValue(ParameterValueType):
    class Meta:
        name = "parameterValue"
        namespace = "http://www.opengis.net/gml"
