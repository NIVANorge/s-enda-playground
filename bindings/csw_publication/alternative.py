from dataclasses import dataclass
from bindings.csw_publication.simple_literal import SimpleLiteral

__NAMESPACE__ = "http://purl.org/dc/terms/"


@dataclass
class Alternative(SimpleLiteral):
    class Meta:
        name = "alternative"
        namespace = "http://purl.org/dc/terms/"
