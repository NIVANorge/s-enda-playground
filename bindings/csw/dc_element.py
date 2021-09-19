from dataclasses import dataclass
from bindings.csw.simple_literal import SimpleLiteral

__NAMESPACE__ = "http://purl.org/dc/elements/1.1/"


@dataclass
class DcElement(SimpleLiteral):
    class Meta:
        name = "DC-element"
        namespace = "http://purl.org/dc/elements/1.1/"
