from dataclasses import dataclass
from bindings.csw.simple_literal import SimpleLiteral

__NAMESPACE__ = "http://purl.org/dc/terms/"


@dataclass
class Temporal(SimpleLiteral):
    class Meta:
        name = "temporal"
        namespace = "http://purl.org/dc/terms/"
