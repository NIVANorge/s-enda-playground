from dataclasses import dataclass
from bindings.gmd.code_type import CodeType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CodeWithAuthorityType(CodeType):
    """
    gml:CodeWithAuthorityType requires that the codeSpace attribute is provided
    in an instance.
    """
