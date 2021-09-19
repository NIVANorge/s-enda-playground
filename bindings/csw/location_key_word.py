from dataclasses import dataclass
from bindings.csw.code_type_2 import CodeType2

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class LocationKeyWord(CodeType2):
    class Meta:
        namespace = "http://www.opengis.net/gml"
