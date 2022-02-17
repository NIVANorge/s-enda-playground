from dataclasses import dataclass, field
from typing import List, Optional
from bindings.wfs.bounding_box import BoundingBox
from bindings.wfs.code_type import CodeType
from bindings.wfs.description_type import DescriptionType
from bindings.wfs.metadata import Metadata
from bindings.wfs.wgs84_bounding_box import Wgs84BoundingBox

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class DatasetDescriptionSummaryBaseType(DescriptionType):
    """Typical dataset metadata in typical Contents section of an OWS service
    metadata (Capabilities) document.

    This type shall be extended and/or restricted if needed for specific
    OWS use, to include the specific Dataset  description metadata
    needed.

    :ivar wgs84_bounding_box: Unordered list of zero or more minimum
        bounding rectangles surrounding coverage data, using the WGS 84
        CRS with decimal degrees and longitude before latitude. If no
        WGS 84 bounding box is recorded for a coverage, any such
        bounding boxes recorded for a higher level in a hierarchy of
        datasets shall apply to this coverage. If WGS 84 bounding
        box(es) are recorded for a coverage, any such bounding boxes
        recorded for a higher level in a hierarchy of datasets shall be
        ignored. For each lowest-level coverage in a hierarchy, at least
        one applicable WGS84BoundingBox shall be either recorded or
        inherited, to simplify searching for datasets that might overlap
        a specified region. If multiple WGS 84 bounding boxes are
        included, this shall be interpreted as the union of the areas of
        these bounding boxes.
    :ivar identifier: Unambiguous identifier or name of this coverage,
        unique for this server.
    :ivar bounding_box: Unordered list of zero or more minimum bounding
        rectangles surrounding coverage data, in AvailableCRSs.  Zero or
        more BoundingBoxes are  allowed in addition to one or more
        WGS84BoundingBoxes to allow more precise specification of the
        Dataset area in AvailableCRSs. These Bounding Boxes shall not
        use any CRS not listed as an AvailableCRS. However, an
        AvailableCRS can be listed without a corresponding Bounding Box.
        If no such bounding box is recorded for a coverage, any such
        bounding boxes recorded for a higher level in a hierarchy of
        datasets shall apply to this coverage. If such bounding box(es)
        are recorded for a coverage, any such bounding boxes recorded
        for a higher level in a hierarchy of datasets shall be ignored.
        If multiple bounding boxes are included with the same CRS, this
        shall be interpreted as the union of the areas of these bounding
        boxes.
    :ivar metadata: Optional unordered list of additional metadata about
        this dataset. A list of optional metadata elements for this
        dataset description could be specified in the Implementation
        Specification for this service.
    :ivar dataset_description_summary: Metadata describing zero or more
        unordered subsidiary datasets available from this server.
    """

    wgs84_bounding_box: List[Wgs84BoundingBox] = field(
        default_factory=list,
        metadata={
            "name": "WGS84BoundingBox",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
        },
    )
    identifier: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "Identifier",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
            "required": True,
        },
    )
    bounding_box: List[BoundingBox] = field(
        default_factory=list,
        metadata={
            "name": "BoundingBox",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
        },
    )
    metadata: List[Metadata] = field(
        default_factory=list,
        metadata={
            "name": "Metadata",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
        },
    )
    dataset_description_summary: List["DatasetDescriptionSummary"] = field(
        default_factory=list,
        metadata={
            "name": "DatasetDescriptionSummary",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
        },
    )


@dataclass
class DatasetDescriptionSummary(DatasetDescriptionSummaryBaseType):
    class Meta:
        namespace = "http://www.opengis.net/ows/1.1"
