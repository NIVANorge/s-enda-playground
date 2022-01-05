from dataclasses import dataclass, field
from typing import List
from bindings.ows.basic_identification_type import BasicIdentificationType
from bindings.ows.bounding_box import BoundingBox
from bindings.ows.wgs84_bounding_box import Wgs84BoundingBox

__NAMESPACE__ = "http://www.opengis.net/ows/2.0"


@dataclass
class IdentificationType(BasicIdentificationType):
    """Extended metadata identifying and describing a set of data.

    This type shall be extended if needed for each specific OWS to
    include additional metadata for each type of dataset. If needed,
    this type should first be restricted for each specific OWS to change
    the multiplicity (or optionality) of some elements.

    :ivar wgs84_bounding_box:
    :ivar bounding_box: Unordered list of zero or more bounding boxes
        whose union describes the extent of this dataset.
    :ivar output_format: Unordered list of zero or more references to
        data formats supported for server outputs.
    :ivar supported_crs:
    :ivar available_crs: Unordered list of zero or more available
        coordinate reference systems.
    """
    wgs84_bounding_box: List[Wgs84BoundingBox] = field(
        default_factory=list,
        metadata={
            "name": "WGS84BoundingBox",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/2.0",
        }
    )
    bounding_box: List[BoundingBox] = field(
        default_factory=list,
        metadata={
            "name": "BoundingBox",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/2.0",
        }
    )
    output_format: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OutputFormat",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/2.0",
            "pattern": r"(application|audio|image|text|video|message|multipart|model)/.+(;\s*.+=.+)*",
        }
    )
    supported_crs: List[str] = field(
        default_factory=list,
        metadata={
            "name": "SupportedCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/2.0",
        }
    )
    available_crs: List[str] = field(
        default_factory=list,
        metadata={
            "name": "AvailableCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/2.0",
        }
    )
