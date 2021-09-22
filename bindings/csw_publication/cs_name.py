from dataclasses import dataclass
from bindings.csw_publication.code_type_2 import CodeType2

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CsName(CodeType2):
    """
    The name by which this coordinate system is identified.
    """
    class Meta:
        name = "csName"
        namespace = "http://www.opengis.net/gml"
