from dataclasses import dataclass
from bindings.csw_publication.simple_literal import SimpleLiteral

__NAMESPACE__ = "http://purl.org/dc/elements/1.1/"


@dataclass
class Language2(SimpleLiteral):
    """A language of the intellectual content of the resource.

    Recommended best practice is to use RFC 3066, which, in conjunction
    with ISO 639, defines two- and three-letter primary language tags
    with optional subtags. Examples include "en" or "eng" for English,
    "akk" for Akkadian, and "en-GB" for English used in the United
    Kingdom.
    """
    class Meta:
        name = "language"
        namespace = "http://purl.org/dc/elements/1.1/"
