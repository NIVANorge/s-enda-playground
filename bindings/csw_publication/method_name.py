from dataclasses import dataclass
from bindings.csw_publication.code_type_2 import CodeType2

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MethodName(CodeType2):
    """
    The name by which this operation method is identified.
    """
    class Meta:
        name = "methodName"
        namespace = "http://www.opengis.net/gml"
