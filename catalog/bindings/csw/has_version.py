from dataclasses import dataclass
from bindings.csw.simple_literal import SimpleLiteral

__NAMESPACE__ = "http://purl.org/dc/terms/"


@dataclass
class HasVersion(SimpleLiteral):
    class Meta:
        name = "hasVersion"
        namespace = "http://purl.org/dc/terms/"
