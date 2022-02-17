from dataclasses import dataclass
from bindings.csw.simple_literal import SimpleLiteral

__NAMESPACE__ = "http://purl.org/dc/terms/"


@dataclass
class DateAccepted(SimpleLiteral):
    class Meta:
        name = "dateAccepted"
        namespace = "http://purl.org/dc/terms/"
