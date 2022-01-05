from dataclasses import dataclass
from bindings.csw.simple_literal import SimpleLiteral

__NAMESPACE__ = "http://purl.org/dc/terms/"


@dataclass
class Medium(SimpleLiteral):
    class Meta:
        name = "medium"
        namespace = "http://purl.org/dc/terms/"
