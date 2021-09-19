from dataclasses import dataclass
from bindings.csw.simple_literal import SimpleLiteral

__NAMESPACE__ = "http://purl.org/dc/terms/"


@dataclass
class Abstract2(SimpleLiteral):
    class Meta:
        name = "abstract"
        namespace = "http://purl.org/dc/terms/"
