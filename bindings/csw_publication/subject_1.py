from dataclasses import dataclass
from bindings.csw_publication.simple_literal import SimpleLiteral

__NAMESPACE__ = "http://purl.org/dc/elements/1.1/"


@dataclass
class Subject1(SimpleLiteral):
    """A topic of the content of the resource.

    Typically, Subject will be expressed as keywords, key phrases, or
    classification codes that describe a topic of the resource.
    Recommended best practice is to select a value from a controlled
    vocabulary or formal classification scheme.
    """
    class Meta:
        name = "subject"
        namespace = "http://purl.org/dc/elements/1.1/"
