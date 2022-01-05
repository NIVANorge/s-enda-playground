from dataclasses import dataclass
from bindings.csw.simple_literal import SimpleLiteral

__NAMESPACE__ = "http://purl.org/dc/terms/"


@dataclass
class IsReplacedBy(SimpleLiteral):
    class Meta:
        name = "isReplacedBy"
        namespace = "http://purl.org/dc/terms/"
