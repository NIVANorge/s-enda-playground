from dataclasses import dataclass
from bindings.csw.simple_literal import SimpleLiteral

__NAMESPACE__ = "http://purl.org/dc/terms/"


@dataclass
class DateCopyrighted(SimpleLiteral):
    class Meta:
        name = "dateCopyrighted"
        namespace = "http://purl.org/dc/terms/"
