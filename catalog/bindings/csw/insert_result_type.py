from dataclasses import dataclass, field
from typing import List, Optional
from bindings.csw.brief_record import BriefRecord

__NAMESPACE__ = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class InsertResultType:
    """Returns a "brief" view of any newly created catalogue records.

    The handle attribute may reference a particular statement in the
    corresponding transaction request.
    """

    brief_record: List[BriefRecord] = field(
        default_factory=list,
        metadata={
            "name": "BriefRecord",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
            "min_occurs": 1,
        },
    )
    handle_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "handleRef",
            "type": "Attribute",
        },
    )
