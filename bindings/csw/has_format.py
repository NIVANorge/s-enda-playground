from dataclasses import dataclass
from bindings.csw.simple_literal import SimpleLiteral

__NAMESPACE__ = "http://purl.org/dc/terms/"


@dataclass
class HasFormat(SimpleLiteral):
    class Meta:
        name = "hasFormat"
        namespace = "http://purl.org/dc/terms/"
