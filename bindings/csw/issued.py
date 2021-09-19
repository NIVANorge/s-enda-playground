from dataclasses import dataclass
from bindings.csw.simple_literal import SimpleLiteral

__NAMESPACE__ = "http://purl.org/dc/terms/"


@dataclass
class Issued(SimpleLiteral):
    class Meta:
        name = "issued"
        namespace = "http://purl.org/dc/terms/"
