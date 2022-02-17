from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/ows"


@dataclass
class Language1:
    """Identifier of a language used by the data(set) contents.

    This language identifier shall be as specified in IETF RFC 1766.
    When this element is omitted, the language used is not identified.
    """

    class Meta:
        name = "Language"
        namespace = "http://www.opengis.net/ows"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
