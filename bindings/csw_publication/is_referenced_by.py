from dataclasses import dataclass
from bindings.csw_publication.simple_literal import SimpleLiteral

__NAMESPACE__ = "http://purl.org/dc/terms/"


@dataclass
class IsReferencedBy(SimpleLiteral):
    class Meta:
        name = "isReferencedBy"
        namespace = "http://purl.org/dc/terms/"
