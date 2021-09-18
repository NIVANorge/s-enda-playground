from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDuration
from generated.csw_discovery import (
    Acknowledgement,
    Constraint,
    RequestBaseType,
)
from generated.record import BriefRecord

__NAMESPACE__ = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class InsertType:
    """Submits one or more records to the catalogue.

    The representation is defined by the application profile. The handle
    attribute may be included to specify a local identifier for the
    action (it must be unique within the context of the transaction).
    """
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        }
    )
    type_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "typeName",
            "type": "Attribute",
        }
    )
    handle: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class RecordPropertyType:
    """
    :ivar name: The Name element contains the name of a property to be
        updated.  The name may be a path expression.
    :ivar value: The Value element contains the replacement value for
        the named property.
    """
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
            "required": True,
        }
    )
    value: Optional[object] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
        }
    )


@dataclass
class TransactionSummaryType:
    """Reports the total number of catalogue items modified by a transaction
    request (i.e, inserted, updated, deleted).

    If the client did not specify a requestId, the server may assign one
    (a URI value).
    """
    total_inserted: Optional[int] = field(
        default=None,
        metadata={
            "name": "totalInserted",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
        }
    )
    total_updated: Optional[int] = field(
        default=None,
        metadata={
            "name": "totalUpdated",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
        }
    )
    total_deleted: Optional[int] = field(
        default=None,
        metadata={
            "name": "totalDeleted",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
        }
    )
    request_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "requestId",
            "type": "Attribute",
        }
    )


@dataclass
class DeleteType:
    """
    Deletes one or more catalogue items that satisfy some set of conditions.
    """
    constraint: Optional[Constraint] = field(
        default=None,
        metadata={
            "name": "Constraint",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
            "required": True,
        }
    )
    type_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "typeName",
            "type": "Attribute",
        }
    )
    handle: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class HarvestType(RequestBaseType):
    """Requests that the catalogue attempt to harvest a resource from some
    network location identified by the source URL.

    Source          - a URL from which the resource is retrieved
    ResourceType    - normally a URI that specifies the type of the resource
    (DCMES v1.1) being harvested if it is known.
    ResourceFormat  - a media type indicating the format of the
    resource being harvested.  The default is
    "application/xml".
    ResponseHandler - a reference to some endpoint to which the
    response shall be forwarded when the
    harvest operation has been completed
    HarvestInterval - an interval expressed using the ISO 8601 syntax;
    it specifies the interval between harvest
    attempts (e.g., P6M indicates an interval of
    six months).
    """
    source: Optional[str] = field(
        default=None,
        metadata={
            "name": "Source",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
            "required": True,
        }
    )
    resource_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "ResourceType",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
            "required": True,
        }
    )
    resource_format: Optional[str] = field(
        default=None,
        metadata={
            "name": "ResourceFormat",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
        }
    )
    harvest_interval: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "HarvestInterval",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
        }
    )
    response_handler: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ResponseHandler",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
        }
    )


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
        }
    )
    handle_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "handleRef",
            "type": "Attribute",
        }
    )


@dataclass
class RecordProperty(RecordPropertyType):
    """
    The RecordProperty element is used to specify the new value of a record
    property in an update statement.
    """
    class Meta:
        namespace = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class Harvest(HarvestType):
    class Meta:
        namespace = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class TransactionResponseType:
    """The response for a transaction request that was successfully completed.

    If the transaction failed for any reason, a service exception report
    indicating a TransactionFailure is returned instead.
    """
    transaction_summary: Optional[TransactionSummaryType] = field(
        default=None,
        metadata={
            "name": "TransactionSummary",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
            "required": True,
        }
    )
    insert_result: List[InsertResultType] = field(
        default_factory=list,
        metadata={
            "name": "InsertResult",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
        }
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class UpdateType:
    """Update statements may replace an entire record or only update part of a
    record:

    1) To replace an existing record, include a new instance of the
    record; 2) To update selected properties of an existing record,
    include a set of RecordProperty elements. The scope of the update
    statement  is determined by the Constraint element. The 'handle' is
    a local identifier for the action.
    """
    other_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        }
    )
    record_property: List[RecordProperty] = field(
        default_factory=list,
        metadata={
            "name": "RecordProperty",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
        }
    )
    constraint: Optional[Constraint] = field(
        default=None,
        metadata={
            "name": "Constraint",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
        }
    )
    handle: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class TransactionResponse(TransactionResponseType):
    class Meta:
        namespace = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class TransactionType(RequestBaseType):
    """Users may insert, update, or delete catalogue entries.

    If the verboseResponse attribute has the value "true", then one or
    more csw:InsertResult elements must be included in the response.
    """
    insert: List[InsertType] = field(
        default_factory=list,
        metadata={
            "name": "Insert",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
            "sequential": True,
        }
    )
    update: List[UpdateType] = field(
        default_factory=list,
        metadata={
            "name": "Update",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
            "sequential": True,
        }
    )
    delete: List[DeleteType] = field(
        default_factory=list,
        metadata={
            "name": "Delete",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
            "sequential": True,
        }
    )
    verbose_response: bool = field(
        default=False,
        metadata={
            "name": "verboseResponse",
            "type": "Attribute",
        }
    )
    request_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "requestId",
            "type": "Attribute",
        }
    )


@dataclass
class HarvestResponseType:
    acknowledgement: Optional[Acknowledgement] = field(
        default=None,
        metadata={
            "name": "Acknowledgement",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
        }
    )
    transaction_response: Optional[TransactionResponse] = field(
        default=None,
        metadata={
            "name": "TransactionResponse",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
        }
    )


@dataclass
class Transaction(TransactionType):
    class Meta:
        namespace = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class HarvestResponse(HarvestResponseType):
    """The content of the response varies depending on the presence of the
    ResponseHandler element.

    If present, then the catalogue should verify the request and respond
    immediately with an csw:Acknowledgement element in the response. The
    catalogue must then attempt to harvest the resource at some later
    time and send the response message to the location specified by the
    value of the ResponseHandler element using the indicated protocol
    (e.g. ftp, mailto, http). If the ResponseHandler element is absent,
    then the catalogue must attempt to harvest the resource immediately
    and include a TransactionResponse element in the response. In any
    case, if the harvest attempt is successful the response shall
    include summary representations of the newly created catalogue
    item(s).
    """
    class Meta:
        namespace = "http://www.opengis.net/cat/csw/2.0.2"
