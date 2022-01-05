from dataclasses import dataclass
from bindings.csw.simple_literal import SimpleLiteral

__NAMESPACE__ = "http://purl.org/dc/terms/"


@dataclass
class IsFormatOf(SimpleLiteral):
    class Meta:
        name = "isFormatOf"
        namespace = "http://purl.org/dc/terms/"
