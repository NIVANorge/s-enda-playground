from dataclasses import dataclass, field
from typing import List, Optional
from bindings.csw.keywords import Keywords

__NAMESPACE__ = "http://www.opengis.net/ows"


@dataclass
class DescriptionType:
    """Human-readable descriptive information for the object it is included
    within.

    This type shall be extended if needed for specific OWS use to
    include additional metadata for each type of information. This type
    shall not be restricted for a specific OWS to change the
    multiplicity (or optionality) of some elements.
    """

    title: Optional[str] = field(
        default=None,
        metadata={
            "name": "Title",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows",
        },
    )
    abstract: Optional[str] = field(
        default=None,
        metadata={
            "name": "Abstract",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows",
        },
    )
    keywords: List[Keywords] = field(
        default_factory=list,
        metadata={
            "name": "Keywords",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows",
        },
    )
