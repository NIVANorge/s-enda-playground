from dataclasses import dataclass
from bindings.csw_publication.abstract_general_parameter_value_type import AbstractGeneralParameterValueType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GeneralParameterValue(AbstractGeneralParameterValueType):
    class Meta:
        name = "_generalParameterValue"
        namespace = "http://www.opengis.net/gml"
