from dataclasses import dataclass
from bindings.csw_publication.code_type_2 import CodeType2

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ParameterName(CodeType2):
    """
    The name by which this operation parameter is identified.
    """
    class Meta:
        name = "parameterName"
        namespace = "http://www.opengis.net/gml"
