from dataclasses import dataclass, field
from typing import List, Optional
from generated.xlink import (
    ActuateType,
    ShowType,
    TypeType,
)

__NAMESPACE__ = "http://www.opengis.net/ows"


@dataclass
class AbstractMetaData:
    """Abstract element containing more metadata about the element that
    includes the containing "metadata" element.

    A specific server implementation, or an Implementation
    Specification, can define concrete elements in the AbstractMetaData
    substitution group.
    """
    class Meta:
        namespace = "http://www.opengis.net/ows"


@dataclass
class BoundingBoxType:
    """XML encoded minimum rectangular bounding box (or region) parameter,
    surrounding all the associated data.

    This type is adapted from the EnvelopeType of GML 3.1, with modified
    contents and documentation for encoding a MINIMUM size box
    SURROUNDING all associated data.

    :ivar lower_corner: Position of the bounding box corner at which the
        value of each coordinate normally is the algebraic minimum
        within this bounding box. In some cases, this position is
        normally displayed at the top, such as the top left for some
        image coordinates. For more information, see Subclauses 10.2.5
        and C.13.
    :ivar upper_corner: Position of the bounding box corner at which the
        value of each coordinate normally is the algebraic maximum
        within this bounding box. In some cases, this position is
        normally displayed at the bottom, such as the bottom right for
        some image coordinates. For more information, see Subclauses
        10.2.5 and C.13.
    :ivar crs: Usually references the definition of a CRS, as specified
        in [OGC Topic 2]. Such a CRS definition can be XML encoded using
        the gml:CoordinateReferenceSystemType in [GML 3.1]. For well
        known references, it is not required that a CRS definition exist
        at the location the URI points to. If no anyURI value is
        included, the applicable CRS must be either: a)      Specified
        outside the bounding box, but inside a data structure that
        includes this bounding box, as specified for a specific OWS use
        of this bounding box type. b)      Fixed and specified in the
        Implementation Specification for a specific OWS use of the
        bounding box type.
    :ivar dimensions: The number of dimensions in this CRS (the length
        of a coordinate sequence in this use of the PositionType). This
        number is specified by the CRS definition, but can also be
        specified here.
    """
    lower_corner: List[float] = field(
        default_factory=list,
        metadata={
            "name": "LowerCorner",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows",
            "required": True,
            "tokens": True,
        }
    )
    upper_corner: List[float] = field(
        default_factory=list,
        metadata={
            "name": "UpperCorner",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows",
            "required": True,
            "tokens": True,
        }
    )
    crs: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    dimensions: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Wgs84BoundingBoxType:
    """XML encoded minimum rectangular bounding box (or region) parameter,
    surrounding all the associated data.

    This box is specialized for use with the 2D WGS 84 coordinate
    reference system with decimal values of longitude and latitude. This
    type is adapted from the general BoundingBoxType, with modified
    contents and documentation for use with the 2D WGS 84 coordinate
    reference system.

    :ivar lower_corner: Position of the bounding box corner at which the
        values of longitude and latitude normally are the algebraic
        minimums within this bounding box. For more information, see
        Subclauses 10.4.5 and C.13.
    :ivar upper_corner: Position of the bounding box corner at which the
        values of longitude and latitude normally are the algebraic
        minimums within this bounding box. For more information, see
        Subclauses 10.4.5 and C.13.
    :ivar crs: This attribute can be included when considered useful.
        When included, this attribute shall reference the 2D WGS 84
        coordinate reference system with longitude before latitude and
        decimal values of longitude and latitude.
    :ivar dimensions: The number of dimensions in this CRS (the length
        of a coordinate sequence in this use of the PositionType). This
        number is specified by the CRS definition, but can also be
        specified here.
    """
    class Meta:
        name = "WGS84BoundingBoxType"

    lower_corner: List[float] = field(
        default_factory=list,
        metadata={
            "name": "LowerCorner",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows",
            "required": True,
            "length": 2,
            "tokens": True,
        }
    )
    upper_corner: List[float] = field(
        default_factory=list,
        metadata={
            "name": "UpperCorner",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows",
            "required": True,
            "length": 2,
            "tokens": True,
        }
    )
    crs: str = field(
        init=False,
        default="urn:ogc:def:crs:OGC:2:84",
        metadata={
            "type": "Attribute",
        }
    )
    dimensions: int = field(
        init=False,
        default=2,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class BoundingBox(BoundingBoxType):
    class Meta:
        namespace = "http://www.opengis.net/ows"


@dataclass
class MetadataType:
    """This element either references or contains more metadata about the
    element that includes this element.

    To reference metadata stored remotely, at least the xlinks:href
    attribute in xlink:simpleAttrs shall be included. Either at least
    one of the attributes in xlink:simpleAttrs or a substitute for the
    AbstractMetaData element shall be included, but not both. An
    Implementation Specification can restrict the contents of this
    element to always be a reference or always contain metadata.
    (Informative: This element was adapted from the metaDataProperty
    element in GML 3.0.)

    :ivar abstract_meta_data:
    :ivar type:
    :ivar href:
    :ivar role:
    :ivar arcrole:
    :ivar title:
    :ivar show:
    :ivar actuate:
    :ivar about: Optional reference to the aspect of the element which
        includes this "metadata" element that this metadata provides
        more information about.
    """
    abstract_meta_data: Optional[AbstractMetaData] = field(
        default=None,
        metadata={
            "name": "AbstractMetaData",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows",
        }
    )
    type: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    about: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Wgs84BoundingBox(Wgs84BoundingBoxType):
    class Meta:
        name = "WGS84BoundingBox"
        namespace = "http://www.opengis.net/ows"


@dataclass
class Metadata(MetadataType):
    class Meta:
        namespace = "http://www.opengis.net/ows"
