from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime
from bindings.csw_publication.abstract_record import AbstractRecord
from bindings.csw_publication.brief_record import BriefRecord
from bindings.csw_publication.dcmirecord import Dcmirecord
from bindings.csw_publication.element_set_type import ElementSetType
from bindings.csw_publication.record import Record
from bindings.csw_publication.summary_record import SummaryRecord

__NAMESPACE__ = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class SearchResultsType:
    """Includes representations of result set members if maxRecords &gt; 0. The
    items must conform to one of the csw:Record views or a profile-specific
    representation.

    resultSetId  - id of the result set (a URI).
    elementSet  - The element set that has been returned
    (i.e., "brief", "summary", "full")
    recordSchema  - schema reference for included records(URI)
    numberOfRecordsMatched  - number of records matched by the query
    numberOfRecordsReturned - number of records returned to client
    nextRecord - position of next record in the result set
    (0 if no records remain).
    expires - the time instant when the result set expires and
    is discarded (ISO 8601 format)
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
    result_set_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "resultSetId",
            "type": "Attribute",
        }
    )
    element_set: Optional[ElementSetType] = field(
        default=None,
        metadata={
            "name": "elementSet",
            "type": "Attribute",
        }
    )
    record_schema: Optional[str] = field(
        default=None,
        metadata={
            "name": "recordSchema",
            "type": "Attribute",
        }
    )
    number_of_records_matched: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfRecordsMatched",
            "type": "Attribute",
            "required": True,
        }
    )
    number_of_records_returned: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfRecordsReturned",
            "type": "Attribute",
            "required": True,
        }
    )
    next_record: Optional[int] = field(
        default=None,
        metadata={
            "name": "nextRecord",
            "type": "Attribute",
        }
    )
    expires: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
