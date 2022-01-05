from dataclasses import dataclass
from bindings.csw.simple_literal import SimpleLiteral

__NAMESPACE__ = "http://purl.org/dc/terms/"


@dataclass
class IsPartOf(SimpleLiteral):
    class Meta:
        name = "isPartOf"
        namespace = "http://purl.org/dc/terms/"
