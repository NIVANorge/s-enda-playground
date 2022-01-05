from dataclasses import dataclass
from bindings.csw.simple_literal import SimpleLiteral

__NAMESPACE__ = "http://purl.org/dc/elements/1.1/"


@dataclass
class Format(SimpleLiteral):
    """The physical or digital manifestation of the resource.

    Typically, Format will include the media-type or dimensions of the
    resource. Format may be used to identify the software, hardware, or
    other equipment needed to display or operate the resource. Examples
    of dimensions include size and duration. Recommended best practice
    is to select a value from a controlled vocabulary (for example, the
    list of Internet Media Types defining computer media formats).
    """
    class Meta:
        name = "format"
        namespace = "http://purl.org/dc/elements/1.1/"
