from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CodeType2:
    """Name or code with an (optional) authority.

    Text token. If the codeSpace attribute is present, then its value
    should identify a dictionary, thesaurus or authority for the term,
    such as the organisation who assigned the value, or the dictionary
    from which it is taken. A text string with an optional codeSpace
    attribute.
    """

    class Meta:
        name = "CodeType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    code_space: Optional[str] = field(
        default=None,
        metadata={
            "name": "codeSpace",
            "type": "Attribute",
        },
    )
