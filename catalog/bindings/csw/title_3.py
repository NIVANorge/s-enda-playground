from dataclasses import dataclass
from bindings.csw.simple_literal import SimpleLiteral

__NAMESPACE__ = "http://purl.org/dc/elements/1.1/"


@dataclass
class Title3(SimpleLiteral):
    """A name given to the resource.

    Typically, Title will be a name by which the resource is formally
    known.
    """

    class Meta:
        name = "title"
        namespace = "http://purl.org/dc/elements/1.1/"
