from dataclasses import dataclass
from bindings.csw_publication.second_defining_parameter_type import SecondDefiningParameterType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class SecondDefiningParameter(SecondDefiningParameterType):
    class Meta:
        name = "secondDefiningParameter"
        namespace = "http://www.opengis.net/gml"
