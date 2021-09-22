from dataclasses import dataclass, field
from typing import List, Optional
from bindings.csw_publication.abstract_2 import Abstract2
from bindings.csw_publication.abstract_record_type import AbstractRecordType
from bindings.csw_publication.alternative import Alternative
from bindings.csw_publication.bibliographic_citation import BibliographicCitation
from bindings.csw_publication.bounding_box_1 import BoundingBox1
from bindings.csw_publication.conforms_to import ConformsTo
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
from bindings.csw_publication.medium import Medium
from bindings.csw_publication.modified import Modified
from bindings.csw_publication.references import References
from bindings.csw_publication.relation import Relation
from bindings.csw_publication.replaces import Replaces
from bindings.csw_publication.requires import Requires
from bindings.csw_publication.spatial import Spatial
from bindings.csw_publication.subject_1 import Subject1
from bindings.csw_publication.title_2 import Title2
from bindings.csw_publication.type import TypeType
from bindings.csw_publication.wgs84_bounding_box import Wgs84BoundingBox

__NAMESPACE__ = "http://www.opengis.net/cat/csw/2.0.2"


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
    identifier: List[Identifier2] = field(
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
    title: List[Title2] = field(
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
    subject: List[Subject1] = field(
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
    abstract: List[Abstract2] = field(
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
    bounding_box: List[BoundingBox1] = field(
        default_factory=list,
        metadata={
            "name": "BoundingBox",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows",
        }
    )
