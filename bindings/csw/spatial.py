from dataclasses import dataclass
from bindings.csw.simple_literal import SimpleLiteral

__NAMESPACE__ = "http://purl.org/dc/terms/"


@dataclass
class Spatial(SimpleLiteral):
    class Meta:
        name = "spatial"
        namespace = "http://purl.org/dc/terms/"
