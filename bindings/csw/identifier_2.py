from dataclasses import dataclass
from bindings.csw.simple_literal import SimpleLiteral

__NAMESPACE__ = "http://purl.org/dc/elements/1.1/"


@dataclass
class Identifier2(SimpleLiteral):
    """An unambiguous reference to the resource within a given context.

    Recommended best practice is to identify the resource by means of a
    string or number conforming to a formal identification system.
    Formal identification systems include but are not limited to the
    Uniform Resource Identifier (URI) (including the Uniform Resource
    Locator (URL)), the Digital Object Identifier (DOI), and the
    International Standard Book Number (ISBN).
    """
    class Meta:
        name = "identifier"
        namespace = "http://purl.org/dc/elements/1.1/"
