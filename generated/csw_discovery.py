from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from xml.etree.ElementTree import QName
from xsdata.models.datatype import XmlDateTime
from generated.filter.pkg_1.pkg_1.pkg_0.filter import Filter
from generated.filter.pkg_1.pkg_1.pkg_0.filter_capabilities import FilterCapabilities
from generated.filter.pkg_1.pkg_1.pkg_0.sort import SortBy
from generated.ows.pkg_1.pkg_0.pkg_0.ows_get_capabilities import (
    CapabilitiesBaseType,
    GetCapabilitiesType as OwsGetCapabilitiesGetCapabilitiesType,
)
from generated.record import (
    AbstractRecord,
    BriefRecord,
    Dcmirecord,
    Record,
    SummaryRecord,
)

__NAMESPACE__ = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class AbstractQueryType:
    pass


@dataclass
class ConceptualSchemeType:
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
            "required": True,
        }
    )
    document: Optional[str] = field(
        default=None,
        metadata={
            "name": "Document",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
            "required": True,
        }
    )
    authority: Optional[str] = field(
        default=None,
        metadata={
            "name": "Authority",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
            "required": True,
        }
    )


@dataclass
class DistributedSearchType:
    """Governs the behaviour of a distributed search.

    hopCount     - the maximum number of message hops before
    the search is terminated. Each catalogue node
    decrements this value when the request is received,
    and must not forward the request if hopCount=0.
    """
    hop_count: int = field(
        default=2,
        metadata={
            "name": "hopCount",
            "type": "Attribute",
        }
    )


@dataclass
class EchoedRequestType:
    """
    Includes a copy of the request message body.
    """
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )


class ElementSetType(Enum):
    """
    Named subsets of catalogue object properties; these views are mapped to a
    specific information model and are defined in an application profile.
    """
    BRIEF = "brief"
    SUMMARY = "summary"
    FULL = "full"


@dataclass
class ListOfValuesType:
    value: List[object] = field(
        default_factory=list,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
            "min_occurs": 1,
        }
    )


@dataclass
class RangeOfValuesType:
    min_value: Optional[object] = field(
        default=None,
        metadata={
            "name": "MinValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
        }
    )
    max_value: Optional[object] = field(
        default=None,
        metadata={
            "name": "MaxValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
        }
    )


@dataclass
class RequestBaseType:
    """Base type for all request messages except GetCapabilities.

    The attributes identify the relevant service type and version.
    """
    service: str = field(
        init=False,
        default="CSW",
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    version: str = field(
        init=False,
        default="2.0.2",
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


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
        }
    )


class ResultType(Enum):
    """
    :cvar RESULTS: Include results in the response.
    :cvar HITS: Provide a result set summary, but no results.
    :cvar VALIDATE: Validate the request and return an Acknowledgement
        message if it is valid. Continue processing the request
        asynchronously.
    """
    RESULTS = "results"
    HITS = "hits"
    VALIDATE = "validate"


@dataclass
class SchemaComponentType:
    """A schema component includes a schema fragment (type definition) or an
    entire schema from some target namespace; the schema language is identified
    by URI.

    If the component is a schema fragment its parent MUST be referenced
    (parentSchema).
    """
    target_namespace: Optional[str] = field(
        default=None,
        metadata={
            "name": "targetNamespace",
            "type": "Attribute",
            "required": True,
        }
    )
    parent_schema: Optional[str] = field(
        default=None,
        metadata={
            "name": "parentSchema",
            "type": "Attribute",
        }
    )
    schema_language: Optional[str] = field(
        default=None,
        metadata={
            "name": "schemaLanguage",
            "type": "Attribute",
            "required": True,
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )


@dataclass
class AbstractQuery(AbstractQueryType):
    class Meta:
        namespace = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class AcknowledgementType:
    """This is a general acknowledgement response message for all requests that
    may be processed in an asynchronous manner.

    EchoedRequest - Echoes the submitted request message
    RequestId     - identifier for polling purposes (if no response
    handler is available, or the URL scheme is
    unsupported)
    """
    echoed_request: Optional[EchoedRequestType] = field(
        default=None,
        metadata={
            "name": "EchoedRequest",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
            "required": True,
        }
    )
    request_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RequestId",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
        }
    )
    time_stamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "timeStamp",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class CapabilitiesType(CapabilitiesBaseType):
    """This type extends ows:CapabilitiesBaseType defined in OGC-05-008 to
    include information about supported OGC filter components.

    A profile may extend this type to describe additional capabilities.
    """
    filter_capabilities: Optional[FilterCapabilities] = field(
        default=None,
        metadata={
            "name": "Filter_Capabilities",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "required": True,
        }
    )


@dataclass
class DescribeRecordResponseType:
    """
    The response contains a list of matching schema components in the requested
    schema language.
    """
    schema_component: List[SchemaComponentType] = field(
        default_factory=list,
        metadata={
            "name": "SchemaComponent",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
        }
    )


@dataclass
class DescribeRecordType(RequestBaseType):
    """This request allows a user to discover elements of the information model
    supported by the catalogue. If no TypeName elements are included, then all
    of the schemas for the information model must be returned.

    schemaLanguage - preferred schema language
    (W3C XML Schema by default)
    outputFormat - preferred output format (application/xml by default)
    """
    type_name: List[QName] = field(
        default_factory=list,
        metadata={
            "name": "TypeName",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
        }
    )
    output_format: str = field(
        default="application/xml",
        metadata={
            "name": "outputFormat",
            "type": "Attribute",
        }
    )
    schema_language: str = field(
        default="http://www.w3.org/XML/Schema",
        metadata={
            "name": "schemaLanguage",
            "type": "Attribute",
        }
    )


@dataclass
class DomainValuesType:
    property_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "PropertyName",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
        }
    )
    parameter_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "ParameterName",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
        }
    )
    list_of_values: Optional[ListOfValuesType] = field(
        default=None,
        metadata={
            "name": "ListOfValues",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
        }
    )
    conceptual_scheme: Optional[ConceptualSchemeType] = field(
        default=None,
        metadata={
            "name": "ConceptualScheme",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
        }
    )
    range_of_values: Optional[RangeOfValuesType] = field(
        default=None,
        metadata={
            "name": "RangeOfValues",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
        }
    )
    type: Optional[QName] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    uom: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class ElementSetNameType:
    value: Optional[ElementSetType] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    type_names: List[QName] = field(
        default_factory=list,
        metadata={
            "name": "typeNames",
            "type": "Attribute",
            "tokens": True,
        }
    )


@dataclass
class GetCapabilitiesType(OwsGetCapabilitiesGetCapabilitiesType):
    """Request for a description of service capabilities.

    See OGC 05-008 for more information.
    """
    service: str = field(
        default="http://www.opengis.net/cat/csw",
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class GetDomainType(RequestBaseType):
    """
    Requests the actual values of some specified request parameter or other
    data element.
    """
    property_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "PropertyName",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
        }
    )
    parameter_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "ParameterName",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
        }
    )


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


@dataclass
class QueryConstraintType:
    """A search constraint that adheres to one of the following syntaxes:

    Filter   - OGC filter expression
    CqlText  - OGC CQL predicate

    :ivar filter:
    :ivar cql_text:
    :ivar version: Query language version
    """
    filter: Optional[Filter] = field(
        default=None,
        metadata={
            "name": "Filter",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    cql_text: Optional[str] = field(
        default=None,
        metadata={
            "name": "CqlText",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
        }
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


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


@dataclass
class Acknowledgement(AcknowledgementType):
    class Meta:
        namespace = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class Capabilities(CapabilitiesType):
    class Meta:
        namespace = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class Constraint(QueryConstraintType):
    class Meta:
        namespace = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class DescribeRecord(DescribeRecordType):
    class Meta:
        namespace = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class DescribeRecordResponse(DescribeRecordResponseType):
    class Meta:
        namespace = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class ElementSetName(ElementSetNameType):
    class Meta:
        namespace = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class GetCapabilities(GetCapabilitiesType):
    class Meta:
        namespace = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class GetDomain(GetDomainType):
    class Meta:
        namespace = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class GetDomainResponseType:
    """Returns the actual values for some property.

    In general this is a subset of the value domain (that is, set of
    permissible values), although in some cases these may be the same.
    """
    domain_values: List[DomainValuesType] = field(
        default_factory=list,
        metadata={
            "name": "DomainValues",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
            "min_occurs": 1,
        }
    )


@dataclass
class GetRecordByIdResponse(GetRecordByIdResponseType):
    class Meta:
        namespace = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class GetRecordsResponseType:
    """The response message for a GetRecords request.

    Some or all of the matching records may be included as children of
    the SearchResults element. The RequestId is only included if the
    client specified it.
    """
    request_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RequestId",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
        }
    )
    search_status: Optional[RequestStatusType] = field(
        default=None,
        metadata={
            "name": "SearchStatus",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
            "required": True,
        }
    )
    search_results: Optional[SearchResultsType] = field(
        default=None,
        metadata={
            "name": "SearchResults",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
            "required": True,
        }
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class GetDomainResponse(GetDomainResponseType):
    class Meta:
        namespace = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class GetRecordByIdType(RequestBaseType):
    """Convenience operation to retrieve default record representations by
    identifier.

    Id - object identifier (a URI) that provides a reference to a
    catalogue item (or a result set if the catalogue supports
    persistent result sets).
    ElementSetName - one of "brief, "summary", or "full"
    """
    id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
            "min_occurs": 1,
        }
    )
    element_set_name: Optional[ElementSetName] = field(
        default=None,
        metadata={
            "name": "ElementSetName",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
        }
    )
    output_format: str = field(
        default="application/xml",
        metadata={
            "name": "outputFormat",
            "type": "Attribute",
        }
    )
    output_schema: Optional[str] = field(
        default=None,
        metadata={
            "name": "outputSchema",
            "type": "Attribute",
        }
    )


@dataclass
class GetRecordsResponse(GetRecordsResponseType):
    class Meta:
        namespace = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class QueryType(AbstractQueryType):
    """Specifies a query to execute against instances of one or more object
    types. A set of ElementName elements may be included to specify an adhoc
    view of the csw:Record instances in the result set. Otherwise, use
    ElementSetName to specify a predefined view. The Constraint element
    contains a query filter expressed in a supported query language. A sorting
    criterion that specifies a property to sort by may be included.

    typeNames - a list of object types to query.
    """
    element_set_name: Optional[ElementSetName] = field(
        default=None,
        metadata={
            "name": "ElementSetName",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
        }
    )
    element_name: List[QName] = field(
        default_factory=list,
        metadata={
            "name": "ElementName",
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
    sort_by: Optional[SortBy] = field(
        default=None,
        metadata={
            "name": "SortBy",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    type_names: List[QName] = field(
        default_factory=list,
        metadata={
            "name": "typeNames",
            "type": "Attribute",
            "required": True,
            "tokens": True,
        }
    )


@dataclass
class GetRecordById(GetRecordByIdType):
    class Meta:
        namespace = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class Query(QueryType):
    class Meta:
        namespace = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class GetRecordsType(RequestBaseType):
    """The principal means of searching the catalogue.

    The matching catalogue entries may be included with the response.
    The client may assign a requestId (absolute URI). A distributed
    search is performed if the DistributedSearch element is present and
    the catalogue is a member of a federation. Profiles may allow
    alternative query expressions.
    """
    distributed_search: Optional[DistributedSearchType] = field(
        default=None,
        metadata={
            "name": "DistributedSearch",
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
    query: Optional[Query] = field(
        default=None,
        metadata={
            "name": "Query",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
        }
    )
    abstract_query: Optional[AbstractQuery] = field(
        default=None,
        metadata={
            "name": "AbstractQuery",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
        }
    )
    other_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        }
    )
    request_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "requestId",
            "type": "Attribute",
        }
    )
    result_type: ResultType = field(
        default=ResultType.HITS,
        metadata={
            "name": "resultType",
            "type": "Attribute",
        }
    )
    output_format: str = field(
        default="application/xml",
        metadata={
            "name": "outputFormat",
            "type": "Attribute",
        }
    )
    output_schema: Optional[str] = field(
        default=None,
        metadata={
            "name": "outputSchema",
            "type": "Attribute",
        }
    )
    start_position: int = field(
        default=1,
        metadata={
            "name": "startPosition",
            "type": "Attribute",
        }
    )
    max_records: int = field(
        default=10,
        metadata={
            "name": "maxRecords",
            "type": "Attribute",
        }
    )


@dataclass
class GetRecords(GetRecordsType):
    class Meta:
        namespace = "http://www.opengis.net/cat/csw/2.0.2"
