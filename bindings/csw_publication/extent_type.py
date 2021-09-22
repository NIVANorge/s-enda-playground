from dataclasses import dataclass, field
from typing import List, Optional
from bindings.csw_publication.bounding_box_2 import BoundingBox2
from bindings.csw_publication.bounding_polygon import BoundingPolygon
from bindings.csw_publication.description_2 import Description2
from bindings.csw_publication.temporal_extent import TemporalExtent
from bindings.csw_publication.vertical_extent import VerticalExtent

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ExtentType:
    """Information about the spatial, vertical, and/or temporal extent of a
    reference system object.

    Constraints: At least one of the elements "description", "boundingBox", "boundingPolygon", "verticalExtent", and temporalExtent" must be included, but more that one can be included when appropriate. Furthermore, more than one "boundingBox", "boundingPolygon", "verticalExtent", and/or temporalExtent" element can be included, with more than one meaning the union of the individual domains.

    :ivar description: Description of spatial and/or temporal extent of
        this object.
    :ivar bounding_box: Unordered list of bounding boxes (or envelopes)
        whose union describes the spatial domain of this object.
    :ivar bounding_polygon: Unordered list of bounding polygons whose
        union describes the spatial domain of this object.
    :ivar vertical_extent: Unordered list of vertical intervals whose
        union describes the spatial domain of this object.
    :ivar temporal_extent: Unordered list of time periods whose union
        describes the spatial domain of this object.
    """
    description: Optional[Description2] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    bounding_box: List[BoundingBox2] = field(
        default_factory=list,
        metadata={
            "name": "boundingBox",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    bounding_polygon: List[BoundingPolygon] = field(
        default_factory=list,
        metadata={
            "name": "boundingPolygon",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    vertical_extent: List[VerticalExtent] = field(
        default_factory=list,
        metadata={
            "name": "verticalExtent",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    temporal_extent: List[TemporalExtent] = field(
        default_factory=list,
        metadata={
            "name": "temporalExtent",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
