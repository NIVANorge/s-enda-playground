from dataclasses import dataclass
from bindings.csw.simple_literal import SimpleLiteral

__NAMESPACE__ = "http://purl.org/dc/terms/"


@dataclass
class Provenance(SimpleLiteral):
    class Meta:
        name = "provenance"
        namespace = "http://purl.org/dc/terms/"
