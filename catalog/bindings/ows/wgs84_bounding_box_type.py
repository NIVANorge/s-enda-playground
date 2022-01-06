from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "http://www.opengis.net/ows/2.0"


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
            "namespace": "http://www.opengis.net/ows/2.0",
            "required": True,
            "length": 2,
            "tokens": True,
        },
    )
    upper_corner: List[float] = field(
        default_factory=list,
        metadata={
            "name": "UpperCorner",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/2.0",
            "required": True,
            "length": 2,
            "tokens": True,
        },
    )
    crs: str = field(
        init=False,
        default="urn:ogc:def:crs:OGC:2:84",
        metadata={
            "type": "Attribute",
        },
    )
    dimensions: int = field(
        init=False,
        default=2,
        metadata={
            "type": "Attribute",
        },
    )
