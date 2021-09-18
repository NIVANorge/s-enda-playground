from dataclasses import dataclass, field
from typing import List, Optional
from generated.ows.pkg_1.pkg_0.pkg_0.ows19115subset import (
    CodeType,
    Keywords,
)
from generated.ows.pkg_1.pkg_0.pkg_0.ows_common import (
    BoundingBox,
    Metadata,
    Wgs84BoundingBox,
)

__NAMESPACE__ = "http://www.opengis.net/ows"


@dataclass
class AccessConstraints:
    """Access constraint applied to assure the protection of privacy or
    intellectual property, or any other restrictions on retrieving or using
    data from or otherwise using this server.

    The reserved value NONE (case insensitive) shall be used to mean no
    access constraints are imposed.
    """
    class Meta:
        namespace = "http://www.opengis.net/ows"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class AvailableCrs:
    class Meta:
        name = "AvailableCRS"
        namespace = "http://www.opengis.net/ows"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class Fees:
    """Fees and terms for retrieving data from or otherwise using this server,
    including the monetary units as specified in ISO 4217.

    The reserved value NONE (case insensitive) shall be used to mean no
    fees or terms.
    """
    class Meta:
        namespace = "http://www.opengis.net/ows"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class Language:
    """Identifier of a language used by the data(set) contents.

    This language identifier shall be as specified in IETF RFC 1766.
    When this element is omitted, the language used is not identified.
    """
    class Meta:
        namespace = "http://www.opengis.net/ows"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class OutputFormat:
    """Reference to a format in which this data can be encoded and transferred.

    More specific parameter names should be used by specific OWS
    specifications wherever applicable. More than one such parameter can
    be included for different purposes.
    """
    class Meta:
        namespace = "http://www.opengis.net/ows"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"(application|audio|image|text|video|message|multipart|model)/.+(;\s*.+=.+)*",
        }
    )


@dataclass
class SupportedCrs:
    """Coordinate reference system in which data from this data(set) or
    resource is available or supported.

    More specific parameter names should be used by specific OWS
    specifications wherever applicable. More than one such parameter can
    be included for different purposes.
    """
    class Meta:
        name = "SupportedCRS"
        namespace = "http://www.opengis.net/ows"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class DescriptionType:
    """Human-readable descriptive information for the object it is included
    within.

    This type shall be extended if needed for specific OWS use to
    include additional metadata for each type of information. This type
    shall not be restricted for a specific OWS to change the
    multiplicity (or optionality) of some elements.
    """
    title: Optional[str] = field(
        default=None,
        metadata={
            "name": "Title",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows",
        }
    )
    abstract: Optional[str] = field(
        default=None,
        metadata={
            "name": "Abstract",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows",
        }
    )
    keywords: List[Keywords] = field(
        default_factory=list,
        metadata={
            "name": "Keywords",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows",
        }
    )


@dataclass
class Identifier(CodeType):
    """
    Unique identifier or name of this dataset.
    """
    class Meta:
        namespace = "http://www.opengis.net/ows"


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
    identifier: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "Identifier",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows",
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
    bounding_box: List[BoundingBox] = field(
        default_factory=list,
        metadata={
            "name": "BoundingBox",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows",
        }
    )
    output_format: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OutputFormat",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows",
            "pattern": r"(application|audio|image|text|video|message|multipart|model)/.+(;\s*.+=.+)*",
        }
    )
    supported_crs: List[str] = field(
        default_factory=list,
        metadata={
            "name": "SupportedCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows",
        }
    )
    available_crs: List[str] = field(
        default_factory=list,
        metadata={
            "name": "AvailableCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows",
        }
    )
    metadata: List[Metadata] = field(
        default_factory=list,
        metadata={
            "name": "Metadata",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows",
        }
    )
