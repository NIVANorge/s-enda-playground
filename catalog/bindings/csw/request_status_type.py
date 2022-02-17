from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class RequestStatusType:
    """This element provides information about the status of the search
    request.

    status    - status of the search
    timestamp - the date and time when the result set was modified
    (ISO 8601 format: YYYY-MM-DDThh:mm:ss[+|-]hh:mm).
    """

    timestamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
