from dataclasses import dataclass
from bindings.csw.simple_literal import SimpleLiteral

__NAMESPACE__ = "http://purl.org/dc/terms/"


@dataclass
class Created(SimpleLiteral):
    class Meta:
        name = "created"
        namespace = "http://purl.org/dc/terms/"
