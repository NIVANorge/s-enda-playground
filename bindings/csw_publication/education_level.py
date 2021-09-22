from dataclasses import dataclass
from bindings.csw_publication.simple_literal import SimpleLiteral

__NAMESPACE__ = "http://purl.org/dc/terms/"


@dataclass
class EducationLevel(SimpleLiteral):
    class Meta:
        name = "educationLevel"
        namespace = "http://purl.org/dc/terms/"
