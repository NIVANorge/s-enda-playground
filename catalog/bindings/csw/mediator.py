from dataclasses import dataclass
from bindings.csw.simple_literal import SimpleLiteral

__NAMESPACE__ = "http://purl.org/dc/terms/"


@dataclass
class Mediator(SimpleLiteral):
    class Meta:
        name = "mediator"
        namespace = "http://purl.org/dc/terms/"
