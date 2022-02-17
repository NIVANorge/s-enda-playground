from dataclasses import dataclass, field
from typing import List, Optional
from xml.etree.ElementTree import QName
from bindings.wfs.abstract_2 import Abstract2
from bindings.wfs.extended_description_type import ExtendedDescriptionType
from bindings.wfs.keywords import Keywords
from bindings.wfs.metadata_urltype import MetadataUrltype
from bindings.wfs.output_format_list_type import OutputFormatListType
from bindings.wfs.title_2 import Title2
from bindings.wfs.wgs84_bounding_box import Wgs84BoundingBox

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class FeatureTypeType:
    name: Optional[QName] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
            "required": True,
        },
    )
    title: List[Title2] = field(
        default_factory=list,
        metadata={
            "name": "Title",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        },
    )
    abstract: List[Abstract2] = field(
        default_factory=list,
        metadata={
            "name": "Abstract",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        },
    )
    keywords: List[Keywords] = field(
        default_factory=list,
        metadata={
            "name": "Keywords",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
        },
    )
    default_crs: Optional[str] = field(
        default=None,
        metadata={
            "name": "DefaultCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        },
    )
    other_crs: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OtherCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        },
    )
    no_crs: Optional[object] = field(
        default=None,
        metadata={
            "name": "NoCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        },
    )
    output_formats: Optional[OutputFormatListType] = field(
        default=None,
        metadata={
            "name": "OutputFormats",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        },
    )
    wgs84_bounding_box: List[Wgs84BoundingBox] = field(
        default_factory=list,
        metadata={
            "name": "WGS84BoundingBox",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
        },
    )
    metadata_url: List[MetadataUrltype] = field(
        default_factory=list,
        metadata={
            "name": "MetadataURL",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        },
    )
    extended_description: Optional[ExtendedDescriptionType] = field(
        default=None,
        metadata={
            "name": "ExtendedDescription",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        },
    )
