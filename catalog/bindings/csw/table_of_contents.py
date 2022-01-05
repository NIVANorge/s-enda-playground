from dataclasses import dataclass
from bindings.csw.simple_literal import SimpleLiteral

__NAMESPACE__ = "http://purl.org/dc/terms/"


@dataclass
class TableOfContents(SimpleLiteral):
    class Meta:
        name = "tableOfContents"
        namespace = "http://purl.org/dc/terms/"
