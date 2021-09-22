from dataclasses import dataclass, field
from typing import List
from bindings.csw_publication.abstract_2 import Abstract2
from bindings.csw_publication.abstract_record_type import AbstractRecordType
from bindings.csw_publication.access_rights import AccessRights
from bindings.csw_publication.alternative import Alternative
from bindings.csw_publication.audience import Audience
from bindings.csw_publication.available import Available
from bindings.csw_publication.bibliographic_citation import BibliographicCitation
from bindings.csw_publication.conforms_to import ConformsTo
from bindings.csw_publication.contributor import Contributor
from bindings.csw_publication.coverage_2 import Coverage2
from bindings.csw_publication.created import Created
from bindings.csw_publication.creator import Creator
from bindings.csw_publication.date import Date
from bindings.csw_publication.date_accepted import DateAccepted
from bindings.csw_publication.date_copyrighted import DateCopyrighted
from bindings.csw_publication.date_submitted import DateSubmitted
from bindings.csw_publication.dc_element import DcElement
from bindings.csw_publication.description_1 import Description1
from bindings.csw_publication.education_level import EducationLevel
from bindings.csw_publication.extent import Extent
from bindings.csw_publication.format import Format
from bindings.csw_publication.has_format import HasFormat
from bindings.csw_publication.has_part import HasPart
from bindings.csw_publication.has_version import HasVersion
from bindings.csw_publication.identifier_2 import Identifier2
from bindings.csw_publication.is_format_of import IsFormatOf
from bindings.csw_publication.is_part_of import IsPartOf
from bindings.csw_publication.is_referenced_by import IsReferencedBy
from bindings.csw_publication.is_replaced_by import IsReplacedBy
from bindings.csw_publication.is_required_by import IsRequiredBy
from bindings.csw_publication.is_version_of import IsVersionOf
from bindings.csw_publication.issued import Issued
from bindings.csw_publication.language_2 import Language2
from bindings.csw_publication.license import License
from bindings.csw_publication.mediator import Mediator
from bindings.csw_publication.medium import Medium
from bindings.csw_publication.modified import Modified
from bindings.csw_publication.provenance import Provenance
from bindings.csw_publication.publisher import Publisher
from bindings.csw_publication.references import References
from bindings.csw_publication.relation import Relation
from bindings.csw_publication.replaces import Replaces
from bindings.csw_publication.requires import Requires
from bindings.csw_publication.rights import Rights
from bindings.csw_publication.rights_holder import RightsHolder
from bindings.csw_publication.source import Source
from bindings.csw_publication.spatial import Spatial
from bindings.csw_publication.subject_1 import Subject1
from bindings.csw_publication.table_of_contents import TableOfContents
from bindings.csw_publication.temporal import Temporal
from bindings.csw_publication.title_2 import Title2
from bindings.csw_publication.type import TypeType
from bindings.csw_publication.valid import Valid

__NAMESPACE__ = "http://www.opengis.net/cat/csw/2.0.2"


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
    coverage: List[Coverage2] = field(
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
    language: List[Language2] = field(
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
    identifier: List[Identifier2] = field(
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
    abstract: List[Abstract2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/terms/",
            "sequential": True,
        }
    )
    description: List[Description1] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://purl.org/dc/elements/1.1/",
            "sequential": True,
        }
    )
    subject: List[Subject1] = field(
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
    title: List[Title2] = field(
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
