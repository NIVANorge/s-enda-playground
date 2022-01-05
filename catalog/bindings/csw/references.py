from dataclasses import dataclass
from bindings.csw.simple_literal import SimpleLiteral

__NAMESPACE__ = "http://purl.org/dc/terms/"


@dataclass
class References(SimpleLiteral):
    class Meta:
        name = "references"
        namespace = "http://purl.org/dc/terms/"
