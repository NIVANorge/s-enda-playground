from dataclasses import dataclass
from bindings.csw.parameter_value_type import ParameterValueType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class UsesValue(ParameterValueType):
    """
    Composition association to a parameter value used by this coordinate
    operation.
    """

    class Meta:
        name = "usesValue"
        namespace = "http://www.opengis.net/gml"
