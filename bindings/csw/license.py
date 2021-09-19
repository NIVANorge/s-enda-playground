from dataclasses import dataclass
from bindings.csw.simple_literal import SimpleLiteral

__NAMESPACE__ = "http://purl.org/dc/terms/"


@dataclass
class License(SimpleLiteral):
    class Meta:
        name = "license"
        namespace = "http://purl.org/dc/terms/"
