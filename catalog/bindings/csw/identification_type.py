from dataclasses import dataclass, field
from typing import List, Optional
from bindings.csw.bounding_box_1 import BoundingBox1
from bindings.csw.description_type import DescriptionType
from bindings.csw.identifier_1 import Identifier1
from bindings.csw.metadata_1 import Metadata1
from bindings.csw.wgs84_bounding_box import Wgs84BoundingBox

__NAMESPACE__ = "http://www.opengis.net/ows"


@dataclass
class IdentificationType(DescriptionType):
    """General metadata identifying and describing a set of data.

    This type shall be extended if needed for each specific OWS to
    include additional metadata for each type of dataset. If needed,
    this type should first be restricted for each specific OWS to change
    the multiplicity (or optionality) of some elements.

    :ivar identifier: Optional unique identifier or name of this
        dataset.
    :ivar wgs84_bounding_box:
    :ivar bounding_box: Unordered list of zero or more bounding boxes
        whose union describes the extent of this dataset.
    :ivar output_format: Unordered list of zero or more references to
        data formats supported for server outputs.
    :ivar supported_crs:
    :ivar available_crs: Unordered list of zero or more available
        coordinate reference systems.
    :ivar metadata: Optional unordered list of additional metadata about
        this data(set). A list of optional metadata elements for this
        data identification could be specified in the Implementation
        Specification for this service.
    """

    identifier: Optional[Identifier1] = field(
        default=None,
        metadata={
            "name": "Identifier",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows",
        },
    )
    wgs84_bounding_box: List[Wgs84BoundingBox] = field(
        default_factory=list,
        metadata={
            "name": "WGS84BoundingBox",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows",
        },
    )
    bounding_box: List[BoundingBox1] = field(
        default_factory=list,
        metadata={
            "name": "BoundingBox",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows",
        },
    )
    output_format: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OutputFormat",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows",
            "pattern": r"(application|audio|image|text|video|message|multipart|model)/.+(;\s*.+=.+)*",
        },
    )
    supported_crs: List[str] = field(
        default_factory=list,
        metadata={
            "name": "SupportedCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows",
        },
    )
    available_crs: List[str] = field(
        default_factory=list,
        metadata={
            "name": "AvailableCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows",
        },
    )
    metadata: List[Metadata1] = field(
        default_factory=list,
        metadata={
            "name": "Metadata",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows",
        },
    )
