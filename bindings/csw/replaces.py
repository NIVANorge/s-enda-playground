from dataclasses import dataclass
from bindings.csw.simple_literal import SimpleLiteral

__NAMESPACE__ = "http://purl.org/dc/terms/"


@dataclass
class Replaces(SimpleLiteral):
    class Meta:
        name = "replaces"
        namespace = "http://purl.org/dc/terms/"
