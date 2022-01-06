from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.opengis.net/ows"


@dataclass
class CodeType1:
    """Name or code with an (optional) authority.

    If the codeSpace attribute is present, its value should reference a
    dictionary, thesaurus, or authority for the name or code, such as
    the organisation who assigned the value, or the dictionary from
    which it is taken. Type copied from basicTypes.xsd of GML 3 with
    documentation edited, for possible use outside the
    ServiceIdentification section of a service metadata document.
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
