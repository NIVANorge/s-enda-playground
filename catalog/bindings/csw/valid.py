from dataclasses import dataclass
from bindings.csw.simple_literal import SimpleLiteral

__NAMESPACE__ = "http://purl.org/dc/terms/"


@dataclass
class Valid(SimpleLiteral):
    class Meta:
        name = "valid"
        namespace = "http://purl.org/dc/terms/"
