from dataclasses import dataclass
from bindings.csw.simple_literal import SimpleLiteral

__NAMESPACE__ = "http://purl.org/dc/terms/"


@dataclass
class IsVersionOf(SimpleLiteral):
    class Meta:
        name = "isVersionOf"
        namespace = "http://purl.org/dc/terms/"
