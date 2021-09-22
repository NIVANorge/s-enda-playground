from dataclasses import dataclass, field
from typing import List
from bindings.csw_publication.bounding_box_1 import BoundingBox1
from bindings.csw_publication.dcmirecord_type import DcmirecordType
from bindings.csw_publication.empty_type import EmptyType
from bindings.csw_publication.wgs84_bounding_box import Wgs84BoundingBox

__NAMESPACE__ = "http://www.opengis.net/cat/csw/2.0.2"


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
    bounding_box: List[BoundingBox1] = field(
        default_factory=list,
        metadata={
            "name": "BoundingBox",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows",
        }
    )
