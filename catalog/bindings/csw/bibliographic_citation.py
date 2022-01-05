from dataclasses import dataclass
from bindings.csw.simple_literal import SimpleLiteral

__NAMESPACE__ = "http://purl.org/dc/terms/"


@dataclass
class BibliographicCitation(SimpleLiteral):
    class Meta:
        name = "bibliographicCitation"
        namespace = "http://purl.org/dc/terms/"
