from dataclasses import dataclass, field
from typing import List
from bindings.csw.abstract_record import AbstractRecord
from bindings.csw.brief_record import BriefRecord
from bindings.csw.dcmirecord import Dcmirecord
from bindings.csw.record import Record
from bindings.csw.summary_record import SummaryRecord

__NAMESPACE__ = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class GetRecordByIdResponseType:
    """Returns a representation of the matching entry.

    If there is no matching record, the response message must be empty.
    """
    record: List[Record] = field(
        default_factory=list,
        metadata={
            "name": "Record",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
        }
    )
    summary_record: List[SummaryRecord] = field(
        default_factory=list,
        metadata={
            "name": "SummaryRecord",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
        }
    )
    brief_record: List[BriefRecord] = field(
        default_factory=list,
        metadata={
            "name": "BriefRecord",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
        }
    )
    dcmirecord: List[Dcmirecord] = field(
        default_factory=list,
        metadata={
            "name": "DCMIRecord",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
        }
    )
    abstract_record: List[AbstractRecord] = field(
        default_factory=list,
        metadata={
            "name": "AbstractRecord",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
        }
    )
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        }
    )
