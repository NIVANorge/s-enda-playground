from dataclasses import dataclass, field
from typing import List, Optional
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

__NAMESPACE__ = "http://purl.org/dc/elements/1.1/"


@dataclass
class SimpleLiteral:
    """This is the default type for all of the DC elements.

    It defines a complexType SimpleLiteral which permits mixed content
    but disallows child elements by use of minOcccurs/maxOccurs.
    However, this complexType does permit the derivation of other types
    which would permit child elements. The scheme attribute may be used
    as a qualifier to reference an encoding scheme that describes the
    value domain for a given property.
    """
    scheme: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
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
class DcElement(SimpleLiteral):
    class Meta:
        name = "DC-element"
        namespace = "http://purl.org/dc/elements/1.1/"


@dataclass
class Contributor(SimpleLiteral):
    """An entity responsible for making contributions to the content of the
    resource.

    Examples of Contributor include a person, an organization, or a
    service. Typically, the name of a Contributor should be used to
    indicate the entity.
    """
    class Meta:
        name = "contributor"
        namespace = "http://purl.org/dc/elements/1.1/"


@dataclass
class Coverage(SimpleLiteral):
    """The extent or scope of the content of the resource.

    Typically, Coverage will include spatial location (a place name or
    geographic coordinates), temporal period (a period label, date, or
    date range), or jurisdiction (such as a named administrative
    entity). Recommended best practice is to select a value from a
    controlled vocabulary (for example, the Thesaurus of Geographic
    Names [TGN]) and to use, where appropriate, named places or time
    periods in preference to numeric identifiers such as sets of
    coordinates or date ranges.
    """
    class Meta:
        name = "coverage"
        namespace = "http://purl.org/dc/elements/1.1/"


@dataclass
class Creator(SimpleLiteral):
    """An entity primarily responsible for making the content of the resource.

    Examples of Creator include a person, an organization, or a service.
    Typically, the name of a Creator should be used to indicate the
    entity.
    """
    class Meta:
        name = "creator"
        namespace = "http://purl.org/dc/elements/1.1/"


@dataclass
class Date(SimpleLiteral):
    """A date of an event in the lifecycle of the resource.

    Typically, Date will be associated with the creation or availability
    of the resource. Recommended best practice for encoding the date
    value is defined in a profile of ISO 8601 and includes (among
    others) dates of the form YYYY-MM-DD.
    """
    class Meta:
        name = "date"
        namespace = "http://purl.org/dc/elements/1.1/"


@dataclass
class Description(SimpleLiteral):
    """An account of the content of the resource.

    Examples of Description include, but are not limited to, an
    abstract, table of contents, reference to a graphical representation
    of content, or free-text account of the content.
    """
    class Meta:
        name = "description"
        namespace = "http://purl.org/dc/elements/1.1/"


@dataclass
class Format(SimpleLiteral):
    """The physical or digital manifestation of the resource.

    Typically, Format will include the media-type or dimensions of the
    resource. Format may be used to identify the software, hardware, or
    other equipment needed to display or operate the resource. Examples
    of dimensions include size and duration. Recommended best practice
    is to select a value from a controlled vocabulary (for example, the
    list of Internet Media Types defining computer media formats).
    """
    class Meta:
        name = "format"
        namespace = "http://purl.org/dc/elements/1.1/"


@dataclass
class Identifier(SimpleLiteral):
    """An unambiguous reference to the resource within a given context.

    Recommended best practice is to identify the resource by means of a
    string or number conforming to a formal identification system.
    Formal identification systems include but are not limited to the
    Uniform Resource Identifier (URI) (including the Uniform Resource
    Locator (URL)), the Digital Object Identifier (DOI), and the
    International Standard Book Number (ISBN).
    """
    class Meta:
        name = "identifier"
        namespace = "http://purl.org/dc/elements/1.1/"


@dataclass
class Language(SimpleLiteral):
    """A language of the intellectual content of the resource.

    Recommended best practice is to use RFC 3066, which, in conjunction
    with ISO 639, defines two- and three-letter primary language tags
    with optional subtags. Examples include "en" or "eng" for English,
    "akk" for Akkadian, and "en-GB" for English used in the United
    Kingdom.
    """
    class Meta:
        name = "language"
        namespace = "http://purl.org/dc/elements/1.1/"


@dataclass
class Publisher(SimpleLiteral):
    """An entity responsible for making the resource available.

    Examples of Publisher include a person, an organization, or a
    service. Typically, the name of a Publisher should be used to
    indicate the entity.
    """
    class Meta:
        name = "publisher"
        namespace = "http://purl.org/dc/elements/1.1/"


@dataclass
class Relation(SimpleLiteral):
    """A reference to a related resource.

    Recommended best practice is to identify the referenced resource by
    means of a string or number conforming to a formal identification
    system.
    """
    class Meta:
        name = "relation"
        namespace = "http://purl.org/dc/elements/1.1/"


@dataclass
class Rights(SimpleLiteral):
    """Information about rights held in and over the resource.

    Typically, Rights will contain a rights management statement for the
    resource, or reference a service providing such information. Rights
    information often encompasses Intellectual Property Rights (IPR),
    Copyright, and various Property Rights. If the Rights element is
    absent, no assumptions may be made about any rights held in or over
    the resource.
    """
    class Meta:
        name = "rights"
        namespace = "http://purl.org/dc/elements/1.1/"


@dataclass
class Source(SimpleLiteral):
    """A Reference to a resource from which the present resource is derived.

    The present resource may be derived from the Source resource in
    whole or in part. Recommended best practice is to identify the
    referenced resource by means of a string or number conforming to a
    formal identification system.
    """
    class Meta:
        name = "source"
        namespace = "http://purl.org/dc/elements/1.1/"


@dataclass
class Subject(SimpleLiteral):
    """A topic of the content of the resource.

    Typically, Subject will be expressed as keywords, key phrases, or
    classification codes that describe a topic of the resource.
    Recommended best practice is to select a value from a controlled
    vocabulary or formal classification scheme.
    """
    class Meta:
        name = "subject"
        namespace = "http://purl.org/dc/elements/1.1/"


@dataclass
class Title(SimpleLiteral):
    """A name given to the resource.

    Typically, Title will be a name by which the resource is formally
    known.
    """
    class Meta:
        name = "title"
        namespace = "http://purl.org/dc/elements/1.1/"


@dataclass
class TypeType(SimpleLiteral):
    """The nature or genre of the content of the resource.

    Type includes terms describing general categories, functions,
    genres, or aggregation levels for content. Recommended best practice
    is to select a value from a controlled vocabulary (for example, the
    DCMI Type Vocabulary). To describe the physical or digital
    manifestation of the resource, use the Format element.
    """
    class Meta:
        name = "type"
        namespace = "http://purl.org/dc/elements/1.1/"


@dataclass
class ElementContainer:
    """
    This type definition is included as a convenience for schema authors who
    need a container element for all of the DC elements.
    """
    class Meta:
        name = "elementContainer"

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
