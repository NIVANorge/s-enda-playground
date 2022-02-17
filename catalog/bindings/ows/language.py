from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/ows/2.0"


@dataclass
class Language:
    """Identifier of a language used by the data(set) contents.

    This language identifier shall be as specified in IETF RFC 4646. The
    language tags shall be either complete 5 character codes (e.g. "en-
    CA"), or abbreviated 2 character codes (e.g. "en"). In addition to
    the RFC 4646 codes, the server shall support the single special
    value "*" which is used to indicate "any language".
    """

    class Meta:
        namespace = "http://www.opengis.net/ows/2.0"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
