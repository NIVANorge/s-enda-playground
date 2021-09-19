from dataclasses import dataclass
from bindings.csw.simple_literal import SimpleLiteral

__NAMESPACE__ = "http://purl.org/dc/terms/"


@dataclass
class Available(SimpleLiteral):
    class Meta:
        name = "available"
        namespace = "http://purl.org/dc/terms/"
