from dataclasses import dataclass, field
from typing import List, Optional
from bindings.csw_publication.abstract_record_type import AbstractRecordType
from bindings.csw_publication.alternative import Alternative
from bindings.csw_publication.bibliographic_citation import BibliographicCitation
from bindings.csw_publication.bounding_box_1 import BoundingBox1
from bindings.csw_publication.identifier_2 import Identifier2
from bindings.csw_publication.title_2 import Title2
from bindings.csw_publication.type import TypeType
from bindings.csw_publication.wgs84_bounding_box import Wgs84BoundingBox

__NAMESPACE__ = "http://www.opengis.net/cat/csw/2.0.2"


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
