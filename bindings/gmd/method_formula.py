from dataclasses import dataclass
from bindings.gmd.code_type import CodeType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MethodFormula(CodeType):
    class Meta:
        name = "methodFormula"
        namespace = "http://www.opengis.net/gml"
