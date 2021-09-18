from dataclasses import dataclass, field
from typing import List, Optional
from generated.csw.pkg_2.pkg_0.pkg_2.rec_dcmes import (
    DcElement,
    Contributor,
    Coverage,
    Creator,
    Date,
    Description,
    Format,
    Identifier,
    Language,
    Publisher,
    Relation,
    Rights,
    Source,
    Subject,
    Title,
    TypeType,
)
from generated.csw.pkg_2.pkg_0.pkg_2.rec_dcterms import (
    Abstract,
    AccessRights,
    Alternative,
    Audience,
    Available,
    BibliographicCitation,
    ConformsTo,
    Created,
    DateAccepted,
    DateCopyrighted,
    DateSubmitted,
    EducationLevel,
    Extent,
    HasFormat,
    HasPart,
    HasVersion,
    IsFormatOf,
    IsPartOf,
    IsReferencedBy,
    IsReplacedBy,
    IsRequiredBy,
    IsVersionOf,
    Issued,
    License,
    Mediator,
    Medium,
    Modified,
    Provenance,
    References,
    Replaces,
    Requires,
    RightsHolder,
    Spatial,
    TableOfContents,
    Temporal,
    Valid,
)
from generated.ows.pkg_1.pkg_0.pkg_0.ows_common import (
    BoundingBox,
    Wgs84BoundingBox,
)

__NAMESPACE__ = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class AbstractRecordType:
    pass


@dataclass
class EmptyType:
    pass


@dataclass
class AbstractRecord(AbstractRecordType):
    class Meta:
        namespace = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class BriefRecordType(AbstractRecordType):
    """This type defines a brief representation of the common record format.

    It extends AbstractRecordType to include only the dc:identifier and
    dc:type properties.
    """
    bibliographic_citation: List[BibliographicCitation] = field(
        default_factory=list,
        metadata={
            "name": "bibliographicCitation",
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
        }
    )
    identifier: List[Identifier] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/elements/1.1/",
        }
    )
    alternative: List[Alternative] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
        }
    )
    title: List[Title] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/elements/1.1/",
        }
    )
    type: Optional[TypeType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/elements/1.1/",
        }
    )
    wgs84_bounding_box: List[Wgs84BoundingBox] = field(
        default_factory=list,
        metadata={
            "name": "WGS84BoundingBox",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows",
        }
    )
    bounding_box: List[BoundingBox] = field(
        default_factory=list,
        metadata={
            "name": "BoundingBox",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows",
        }
    )


@dataclass
class DcmirecordType(AbstractRecordType):
    """
    This type encapsulates all of the standard DCMI metadata terms, including
    the Dublin Core refinements; these terms may be mapped to the profile-
    specific information model.
    """
    class Meta:
        name = "DCMIRecordType"

    rights_holder: List[RightsHolder] = field(
        default_factory=list,
        metadata={
            "name": "rightsHolder",
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
            "sequential": True,
        }
    )
    provenance: List[Provenance] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
            "sequential": True,
        }
    )
    mediator: List[Mediator] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
            "sequential": True,
        }
    )
    education_level: List[EducationLevel] = field(
        default_factory=list,
        metadata={
            "name": "educationLevel",
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
            "sequential": True,
        }
    )
    audience: List[Audience] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
            "sequential": True,
        }
    )
    license: List[License] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
            "sequential": True,
        }
    )
    access_rights: List[AccessRights] = field(
        default_factory=list,
        metadata={
            "name": "accessRights",
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
            "sequential": True,
        }
    )
    rights: List[Rights] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/elements/1.1/",
            "sequential": True,
        }
    )
    temporal: List[Temporal] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
            "sequential": True,
        }
    )
    spatial: List[Spatial] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
            "sequential": True,
        }
    )
    coverage: List[Coverage] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/elements/1.1/",
            "sequential": True,
        }
    )
    requires: List[Requires] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
            "sequential": True,
        }
    )
    replaces: List[Replaces] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
            "sequential": True,
        }
    )
    references: List[References] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
            "sequential": True,
        }
    )
    is_version_of: List[IsVersionOf] = field(
        default_factory=list,
        metadata={
            "name": "isVersionOf",
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
            "sequential": True,
        }
    )
    is_required_by: List[IsRequiredBy] = field(
        default_factory=list,
        metadata={
            "name": "isRequiredBy",
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
            "sequential": True,
        }
    )
    is_replaced_by: List[IsReplacedBy] = field(
        default_factory=list,
        metadata={
            "name": "isReplacedBy",
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
            "sequential": True,
        }
    )
    is_referenced_by: List[IsReferencedBy] = field(
        default_factory=list,
        metadata={
            "name": "isReferencedBy",
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
            "sequential": True,
        }
    )
    is_part_of: List[IsPartOf] = field(
        default_factory=list,
        metadata={
            "name": "isPartOf",
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
            "sequential": True,
        }
    )
    is_format_of: List[IsFormatOf] = field(
        default_factory=list,
        metadata={
            "name": "isFormatOf",
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
            "sequential": True,
        }
    )
    has_version: List[HasVersion] = field(
        default_factory=list,
        metadata={
            "name": "hasVersion",
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
            "sequential": True,
        }
    )
    has_part: List[HasPart] = field(
        default_factory=list,
        metadata={
            "name": "hasPart",
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
            "sequential": True,
        }
    )
    has_format: List[HasFormat] = field(
        default_factory=list,
        metadata={
            "name": "hasFormat",
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
            "sequential": True,
        }
    )
    conforms_to: List[ConformsTo] = field(
        default_factory=list,
        metadata={
            "name": "conformsTo",
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
            "sequential": True,
        }
    )
    relation: List[Relation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/elements/1.1/",
            "sequential": True,
        }
    )
    language: List[Language] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/elements/1.1/",
            "sequential": True,
        }
    )
    source: List[Source] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/elements/1.1/",
            "sequential": True,
        }
    )
    bibliographic_citation: List[BibliographicCitation] = field(
        default_factory=list,
        metadata={
            "name": "bibliographicCitation",
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
            "sequential": True,
        }
    )
    identifier: List[Identifier] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/elements/1.1/",
            "sequential": True,
        }
    )
    medium: List[Medium] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
            "sequential": True,
        }
    )
    extent: List[Extent] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
            "sequential": True,
        }
    )
    format: List[Format] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/elements/1.1/",
            "sequential": True,
        }
    )
    type: List[TypeType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/elements/1.1/",
            "sequential": True,
        }
    )
    valid: List[Valid] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
            "sequential": True,
        }
    )
    modified: List[Modified] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
            "sequential": True,
        }
    )
    issued: List[Issued] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
            "sequential": True,
        }
    )
    date_submitted: List[DateSubmitted] = field(
        default_factory=list,
        metadata={
            "name": "dateSubmitted",
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
            "sequential": True,
        }
    )
    date_copyrighted: List[DateCopyrighted] = field(
        default_factory=list,
        metadata={
            "name": "dateCopyrighted",
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
            "sequential": True,
        }
    )
    date_accepted: List[DateAccepted] = field(
        default_factory=list,
        metadata={
            "name": "dateAccepted",
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
            "sequential": True,
        }
    )
    created: List[Created] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
            "sequential": True,
        }
    )
    available: List[Available] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
            "sequential": True,
        }
    )
    date: List[Date] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/elements/1.1/",
            "sequential": True,
        }
    )
    contributor: List[Contributor] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/elements/1.1/",
            "sequential": True,
        }
    )
    publisher: List[Publisher] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/elements/1.1/",
            "sequential": True,
        }
    )
    table_of_contents: List[TableOfContents] = field(
        default_factory=list,
        metadata={
            "name": "tableOfContents",
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
            "sequential": True,
        }
    )
    abstract: List[Abstract] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
            "sequential": True,
        }
    )
    description: List[Description] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/elements/1.1/",
            "sequential": True,
        }
    )
    subject: List[Subject] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/elements/1.1/",
            "sequential": True,
        }
    )
    creator: List[Creator] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/elements/1.1/",
            "sequential": True,
        }
    )
    alternative: List[Alternative] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
            "sequential": True,
        }
    )
    title: List[Title] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/elements/1.1/",
            "sequential": True,
        }
    )
    dc_element: List[DcElement] = field(
        default_factory=list,
        metadata={
            "name": "DC-element",
            "type": "Element",
            "namespace": "http://purl.org/dc/elements/1.1/",
            "sequential": True,
        }
    )


@dataclass
class SummaryRecordType(AbstractRecordType):
    """This type defines a summary representation of the common record format.

    It extends AbstractRecordType to include the core properties.
    """
    bibliographic_citation: List[BibliographicCitation] = field(
        default_factory=list,
        metadata={
            "name": "bibliographicCitation",
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
        }
    )
    identifier: List[Identifier] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/elements/1.1/",
        }
    )
    alternative: List[Alternative] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
        }
    )
    title: List[Title] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/elements/1.1/",
        }
    )
    type: Optional[TypeType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/elements/1.1/",
        }
    )
    subject: List[Subject] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/elements/1.1/",
        }
    )
    medium: List[Medium] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
        }
    )
    extent: List[Extent] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
        }
    )
    format: List[Format] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/elements/1.1/",
        }
    )
    requires: List[Requires] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
        }
    )
    replaces: List[Replaces] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
        }
    )
    references: List[References] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
        }
    )
    is_version_of: List[IsVersionOf] = field(
        default_factory=list,
        metadata={
            "name": "isVersionOf",
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
        }
    )
    is_required_by: List[IsRequiredBy] = field(
        default_factory=list,
        metadata={
            "name": "isRequiredBy",
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
        }
    )
    is_replaced_by: List[IsReplacedBy] = field(
        default_factory=list,
        metadata={
            "name": "isReplacedBy",
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
        }
    )
    is_referenced_by: List[IsReferencedBy] = field(
        default_factory=list,
        metadata={
            "name": "isReferencedBy",
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
        }
    )
    is_part_of: List[IsPartOf] = field(
        default_factory=list,
        metadata={
            "name": "isPartOf",
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
        }
    )
    is_format_of: List[IsFormatOf] = field(
        default_factory=list,
        metadata={
            "name": "isFormatOf",
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
        }
    )
    has_version: List[HasVersion] = field(
        default_factory=list,
        metadata={
            "name": "hasVersion",
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
        }
    )
    has_part: List[HasPart] = field(
        default_factory=list,
        metadata={
            "name": "hasPart",
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
        }
    )
    has_format: List[HasFormat] = field(
        default_factory=list,
        metadata={
            "name": "hasFormat",
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
        }
    )
    conforms_to: List[ConformsTo] = field(
        default_factory=list,
        metadata={
            "name": "conformsTo",
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
        }
    )
    relation: List[Relation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/elements/1.1/",
        }
    )
    modified: List[Modified] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
        }
    )
    abstract: List[Abstract] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
        }
    )
    spatial: List[Spatial] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
        }
    )
    wgs84_bounding_box: List[Wgs84BoundingBox] = field(
        default_factory=list,
        metadata={
            "name": "WGS84BoundingBox",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows",
        }
    )
    bounding_box: List[BoundingBox] = field(
        default_factory=list,
        metadata={
            "name": "BoundingBox",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows",
        }
    )


@dataclass
class BriefRecord(BriefRecordType):
    class Meta:
        namespace = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class Dcmirecord(DcmirecordType):
    class Meta:
        name = "DCMIRecord"
        namespace = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class RecordType(DcmirecordType):
    """
    This type extends DCMIRecordType to add ows:BoundingBox; it may be used to
    specify a spatial envelope for the catalogued resource.
    """
    any_text: List[EmptyType] = field(
        default_factory=list,
        metadata={
            "name": "AnyText",
            "type": "Element",
            "namespace": "http://www.opengis.net/cat/csw/2.0.2",
        }
    )
    wgs84_bounding_box: List[Wgs84BoundingBox] = field(
        default_factory=list,
        metadata={
            "name": "WGS84BoundingBox",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows",
        }
    )
    bounding_box: List[BoundingBox] = field(
        default_factory=list,
        metadata={
            "name": "BoundingBox",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows",
        }
    )


@dataclass
class SummaryRecord(SummaryRecordType):
    class Meta:
        namespace = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class Record(RecordType):
    class Meta:
        namespace = "http://www.opengis.net/cat/csw/2.0.2"
