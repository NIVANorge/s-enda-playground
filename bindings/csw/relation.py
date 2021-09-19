from dataclasses import dataclass
from bindings.csw.simple_literal import SimpleLiteral

__NAMESPACE__ = "http://purl.org/dc/elements/1.1/"


@dataclass
class Relation(SimpleLiteral):
    """A reference to a related resource.

    Recommended best practice is to identify the referenced resource by
    means of a string or number conforming to a formal identification
    system.
    """
    class Meta:
        name = "relation"
        namespace = "http://purl.org/dc/elements/1.1/"
