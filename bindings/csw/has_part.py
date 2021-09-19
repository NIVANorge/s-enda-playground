from dataclasses import dataclass
from bindings.csw.simple_literal import SimpleLiteral

__NAMESPACE__ = "http://purl.org/dc/terms/"


@dataclass
class HasPart(SimpleLiteral):
    class Meta:
        name = "hasPart"
        namespace = "http://purl.org/dc/terms/"
