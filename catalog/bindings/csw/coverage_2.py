from dataclasses import dataclass
from bindings.csw.simple_literal import SimpleLiteral

__NAMESPACE__ = "http://purl.org/dc/elements/1.1/"


@dataclass
class Coverage2(SimpleLiteral):
    """The extent or scope of the content of the resource.

    Typically, Coverage will include spatial location (a place name or
    geographic coordinates), temporal period (a period label, date, or
    date range), or jurisdiction (such as a named administrative
    entity). Recommended best practice is to select a value from a
    controlled vocabulary (for example, the Thesaurus of Geographic
    Names [TGN]) and to use, where appropriate, named places or time
    periods in preference to numeric identifiers such as sets of
    coordinates or date ranges.
    """

    class Meta:
        name = "coverage"
        namespace = "http://purl.org/dc/elements/1.1/"
