from dataclasses import dataclass, field
from typing import List
from bindings.csw.abstract_2 import Abstract2
from bindings.csw.access_rights import AccessRights
from bindings.csw.alternative import Alternative
from bindings.csw.audience import Audience
from bindings.csw.available import Available
from bindings.csw.bibliographic_citation import BibliographicCitation
from bindings.csw.conforms_to import ConformsTo
from bindings.csw.contributor import Contributor
from bindings.csw.coverage_2 import Coverage2
from bindings.csw.created import Created
from bindings.csw.creator import Creator
from bindings.csw.date import Date
from bindings.csw.date_accepted import DateAccepted
from bindings.csw.date_copyrighted import DateCopyrighted
from bindings.csw.date_submitted import DateSubmitted
from bindings.csw.dc_element import DcElement
from bindings.csw.description_2 import Description2
from bindings.csw.education_level import EducationLevel
from bindings.csw.extent import Extent
from bindings.csw.format import Format
from bindings.csw.has_format import HasFormat
from bindings.csw.has_part import HasPart
from bindings.csw.has_version import HasVersion
from bindings.csw.identifier_2 import Identifier2
from bindings.csw.is_format_of import IsFormatOf
from bindings.csw.is_part_of import IsPartOf
from bindings.csw.is_referenced_by import IsReferencedBy
from bindings.csw.is_replaced_by import IsReplacedBy
from bindings.csw.is_required_by import IsRequiredBy
from bindings.csw.is_version_of import IsVersionOf
from bindings.csw.issued import Issued
from bindings.csw.language_2 import Language2
from bindings.csw.license import License
from bindings.csw.mediator import Mediator
from bindings.csw.medium import Medium
from bindings.csw.modified import Modified
from bindings.csw.provenance import Provenance
from bindings.csw.publisher import Publisher
from bindings.csw.references import References
from bindings.csw.relation import Relation
from bindings.csw.replaces import Replaces
from bindings.csw.requires import Requires
from bindings.csw.rights import Rights
from bindings.csw.rights_holder import RightsHolder
from bindings.csw.source import Source
from bindings.csw.spatial import Spatial
from bindings.csw.subject_2 import Subject2
from bindings.csw.table_of_contents import TableOfContents
from bindings.csw.temporal import Temporal
from bindings.csw.title_3 import Title3
from bindings.csw.type import TypeType
from bindings.csw.valid import Valid

__NAMESPACE__ = "http://purl.org/dc/elements/1.1/"


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
        },
    )
    provenance: List[Provenance] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
            "sequential": True,
        },
    )
    mediator: List[Mediator] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
            "sequential": True,
        },
    )
    education_level: List[EducationLevel] = field(
        default_factory=list,
        metadata={
            "name": "educationLevel",
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
            "sequential": True,
        },
    )
    audience: List[Audience] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
            "sequential": True,
        },
    )
    license: List[License] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
            "sequential": True,
        },
    )
    access_rights: List[AccessRights] = field(
        default_factory=list,
        metadata={
            "name": "accessRights",
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
            "sequential": True,
        },
    )
    rights: List[Rights] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/elements/1.1/",
            "sequential": True,
        },
    )
    temporal: List[Temporal] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
            "sequential": True,
        },
    )
    spatial: List[Spatial] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
            "sequential": True,
        },
    )
    coverage: List[Coverage2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/elements/1.1/",
            "sequential": True,
        },
    )
    requires: List[Requires] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
            "sequential": True,
        },
    )
    replaces: List[Replaces] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
            "sequential": True,
        },
    )
    references: List[References] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
            "sequential": True,
        },
    )
    is_version_of: List[IsVersionOf] = field(
        default_factory=list,
        metadata={
            "name": "isVersionOf",
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
            "sequential": True,
        },
    )
    is_required_by: List[IsRequiredBy] = field(
        default_factory=list,
        metadata={
            "name": "isRequiredBy",
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
            "sequential": True,
        },
    )
    is_replaced_by: List[IsReplacedBy] = field(
        default_factory=list,
        metadata={
            "name": "isReplacedBy",
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
            "sequential": True,
        },
    )
    is_referenced_by: List[IsReferencedBy] = field(
        default_factory=list,
        metadata={
            "name": "isReferencedBy",
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
            "sequential": True,
        },
    )
    is_part_of: List[IsPartOf] = field(
        default_factory=list,
        metadata={
            "name": "isPartOf",
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
            "sequential": True,
        },
    )
    is_format_of: List[IsFormatOf] = field(
        default_factory=list,
        metadata={
            "name": "isFormatOf",
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
            "sequential": True,
        },
    )
    has_version: List[HasVersion] = field(
        default_factory=list,
        metadata={
            "name": "hasVersion",
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
            "sequential": True,
        },
    )
    has_part: List[HasPart] = field(
        default_factory=list,
        metadata={
            "name": "hasPart",
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
            "sequential": True,
        },
    )
    has_format: List[HasFormat] = field(
        default_factory=list,
        metadata={
            "name": "hasFormat",
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
            "sequential": True,
        },
    )
    conforms_to: List[ConformsTo] = field(
        default_factory=list,
        metadata={
            "name": "conformsTo",
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
            "sequential": True,
        },
    )
    relation: List[Relation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/elements/1.1/",
            "sequential": True,
        },
    )
    language: List[Language2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/elements/1.1/",
            "sequential": True,
        },
    )
    source: List[Source] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/elements/1.1/",
            "sequential": True,
        },
    )
    bibliographic_citation: List[BibliographicCitation] = field(
        default_factory=list,
        metadata={
            "name": "bibliographicCitation",
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
            "sequential": True,
        },
    )
    identifier: List[Identifier2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/elements/1.1/",
            "sequential": True,
        },
    )
    medium: List[Medium] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
            "sequential": True,
        },
    )
    extent: List[Extent] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
            "sequential": True,
        },
    )
    format: List[Format] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/elements/1.1/",
            "sequential": True,
        },
    )
    type: List[TypeType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/elements/1.1/",
            "sequential": True,
        },
    )
    valid: List[Valid] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
            "sequential": True,
        },
    )
    modified: List[Modified] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
            "sequential": True,
        },
    )
    issued: List[Issued] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
            "sequential": True,
        },
    )
    date_submitted: List[DateSubmitted] = field(
        default_factory=list,
        metadata={
            "name": "dateSubmitted",
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
            "sequential": True,
        },
    )
    date_copyrighted: List[DateCopyrighted] = field(
        default_factory=list,
        metadata={
            "name": "dateCopyrighted",
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
            "sequential": True,
        },
    )
    date_accepted: List[DateAccepted] = field(
        default_factory=list,
        metadata={
            "name": "dateAccepted",
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
            "sequential": True,
        },
    )
    created: List[Created] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
            "sequential": True,
        },
    )
    available: List[Available] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
            "sequential": True,
        },
    )
    date: List[Date] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/elements/1.1/",
            "sequential": True,
        },
    )
    contributor: List[Contributor] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/elements/1.1/",
            "sequential": True,
        },
    )
    publisher: List[Publisher] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/elements/1.1/",
            "sequential": True,
        },
    )
    table_of_contents: List[TableOfContents] = field(
        default_factory=list,
        metadata={
            "name": "tableOfContents",
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
            "sequential": True,
        },
    )
    abstract: List[Abstract2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
            "sequential": True,
        },
    )
    description: List[Description2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/elements/1.1/",
            "sequential": True,
        },
    )
    subject: List[Subject2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/elements/1.1/",
            "sequential": True,
        },
    )
    creator: List[Creator] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/elements/1.1/",
            "sequential": True,
        },
    )
    alternative: List[Alternative] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
            "sequential": True,
        },
    )
    title: List[Title3] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/elements/1.1/",
            "sequential": True,
        },
    )
    dc_element: List[DcElement] = field(
        default_factory=list,
        metadata={
            "name": "DC-element",
            "type": "Element",
            "namespace": "http://purl.org/dc/elements/1.1/",
            "sequential": True,
        },
    )
