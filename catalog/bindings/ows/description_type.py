from dataclasses import dataclass, field
from typing import List
from bindings.ows.abstract import Abstract
from bindings.ows.keywords import Keywords
from bindings.ows.title_1 import Title1

__NAMESPACE__ = "http://www.opengis.net/ows/2.0"


@dataclass
class DescriptionType:
    """Human-readable descriptive information for the object it is included
    within.

    This type shall be extended if needed for specific OWS use to
    include additional metadata for each type of information. This type
    shall not be restricted for a specific OWS to change the
    multiplicity (or optionality) of some elements. If the xml:lang
    attribute is not included in a Title, Abstract or Keyword element,
    then no language is specified for that element unless specified by
    another means. All Title, Abstract and Keyword elements in the same
    Description that share the same xml:lang attribute value represent
    the description of the parent object in that language. Multiple
    Title or Abstract elements shall not exist in the same Description
    with the same xml:lang attribute value unless otherwise specified.
    """

    title: List[Title1] = field(
        default_factory=list,
        metadata={
            "name": "Title",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/2.0",
        },
    )
    abstract: List[Abstract] = field(
        default_factory=list,
        metadata={
            "name": "Abstract",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/2.0",
        },
    )
    keywords: List[Keywords] = field(
        default_factory=list,
        metadata={
            "name": "Keywords",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/2.0",
        },
    )
