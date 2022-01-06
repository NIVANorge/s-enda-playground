from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "http://www.opengis.net/ows/2.0"


@dataclass
class TelephoneType:
    """
    Telephone numbers for contacting the responsible individual or
    organization.

    :ivar voice: Telephone number by which individuals can speak to the
        responsible organization or individual.
    :ivar facsimile: Telephone number of a facsimile machine for the
        responsible organization or individual.
    """

    voice: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Voice",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/2.0",
        },
    )
    facsimile: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Facsimile",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/2.0",
        },
    )
