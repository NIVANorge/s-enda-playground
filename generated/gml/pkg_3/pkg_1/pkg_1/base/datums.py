from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlDate, XmlDateTime
from generated.gml.pkg_3.pkg_1.pkg_1.base.basic_types import (
    CodeType,
    MeasureType,
)
from generated.gml.pkg_3.pkg_1.pkg_1.base.coordinate_operations import (
    CoordinateOperationName,
    GroupName,
    MethodName,
    ParameterName,
)
from generated.gml.pkg_3.pkg_1.pkg_1.base.coordinate_systems import CsName
from generated.gml.pkg_3.pkg_1.pkg_1.base.gml_base import (
    Description,
    MetaDataProperty,
    Name,
)
from generated.gml.pkg_3.pkg_1.pkg_1.base.measures import AngleChoiceType
from generated.gml.pkg_3.pkg_1.pkg_1.base.reference_systems import (
    IdentifierType,
    Remarks,
    SrsName,
    ValidArea,
)
from generated.xlink import (
    ActuateType,
    ShowType,
    TypeType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


class IsSphereValue(Enum):
    SPHERE = "sphere"


@dataclass
class Origin:
    """
    The date and time origin of this temporal datum.
    """
    class Meta:
        name = "origin"
        namespace = "http://www.opengis.net/gml"

    value: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class RealizationEpoch:
    """The time after which this datum definition is valid.

    This time may be precise (e.g. 1997.0 for IRTF97) or merely a year
    (e.g. 1983 for NAD83). In the latter case, the epoch usually refers
    to the year in which a major recalculation of the geodetic control
    network, underlying the datum, was executed or initiated. An old
    datum can remain valid after a new datum is defined. Alternatively,
    a datum may be superseded by a later datum, in which case the
    realization epoch for the new datum defines the upper limit for the
    validity of the superseded datum.
    """
    class Meta:
        name = "realizationEpoch"
        namespace = "http://www.opengis.net/gml"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class PixelInCellType(CodeType):
    """
    Specification of the way an image grid is associated with the image data
    attributes.
    """


@dataclass
class VerticalDatumTypeType(CodeType):
    """
    Type of a vertical datum.
    """


@dataclass
class AnchorPoint(CodeType):
    """Description, possibly including coordinates, of the point or points used
    to anchor the datum to the Earth. Also known as the "origin", especially
    for engineering and image datums. The codeSpace attribute can be used to
    reference a source of more detailed on this point or surface, or on a set
    of such descriptions.

    - For a geodetic datum, this point is also known as the fundamental point, which is traditionally the point where the relationship between geoid and ellipsoid is defined. In some cases, the "fundamental point" may consist of a number of points. In those cases, the parameters defining the geoid/ellipsoid relationship have been averaged for these points, and the averages adopted as the datum definition.
    - For an engineering datum, the anchor point may be a physical point, or it may be a point with defined coordinates in another CRS. When appropriate, the coordinates of this anchor point can be referenced in another document, such as referencing a GML feature that references or includes a point position.
    - For an image datum, the anchor point is usually either the centre of the image or the corner of the image.
    - For a temporal datum, this attribute is not defined. Instead of the anchor point, a temporal datum carries a separate time origin of type DateTime.
    """
    class Meta:
        name = "anchorPoint"
        namespace = "http://www.opengis.net/gml"


@dataclass
class DatumId(IdentifierType):
    """
    An identification of a datum.
    """
    class Meta:
        name = "datumID"
        namespace = "http://www.opengis.net/gml"


@dataclass
class DatumName(CodeType):
    """
    The name by which this datum is identified.
    """
    class Meta:
        name = "datumName"
        namespace = "http://www.opengis.net/gml"


@dataclass
class EllipsoidId(IdentifierType):
    """
    An identification of an ellipsoid.
    """
    class Meta:
        name = "ellipsoidID"
        namespace = "http://www.opengis.net/gml"


@dataclass
class EllipsoidName(CodeType):
    """
    The name by which this ellipsoid is identified.
    """
    class Meta:
        name = "ellipsoidName"
        namespace = "http://www.opengis.net/gml"


@dataclass
class GreenwichLongitude(AngleChoiceType):
    """Longitude of the prime meridian measured from the Greenwich meridian,
    positive eastward.

    The greenwichLongitude most common value is zero, and that value
    shall be used when the meridianName value is Greenwich.
    """
    class Meta:
        name = "greenwichLongitude"
        namespace = "http://www.opengis.net/gml"


@dataclass
class InverseFlattening(MeasureType):
    """Inverse flattening value of the ellipsoid.

    Value is a scale factor (or ratio) that has no physical unit. Uses
    the MeasureType with the restriction that the unit of measure
    referenced by uom must be suitable for a scale factor, such as
    percent, permil, or parts-per-million.
    """
    class Meta:
        name = "inverseFlattening"
        namespace = "http://www.opengis.net/gml"


@dataclass
class IsSphere:
    """The ellipsoid is degenerate and is actually a sphere.

    The sphere is completely defined by the semi-major axis, which is
    the radius of the sphere.
    """
    class Meta:
        name = "isSphere"
        namespace = "http://www.opengis.net/gml"

    value: Optional[IsSphereValue] = field(
        default=None
    )


@dataclass
class MeridianId(IdentifierType):
    """
    An identification of a prime meridian.
    """
    class Meta:
        name = "meridianID"
        namespace = "http://www.opengis.net/gml"


@dataclass
class MeridianName(CodeType):
    """The name by which this prime meridian is identified.

    The meridianName most common value is Greenwich, and that value
    shall be used when the greenwichLongitude value is zero.
    """
    class Meta:
        name = "meridianName"
        namespace = "http://www.opengis.net/gml"


@dataclass
class SemiMajorAxis(MeasureType):
    """Length of the semi-major axis of the ellipsoid, with its units.

    Uses the MeasureType with the restriction that the unit of measure
    referenced by uom must be suitable for a length, such as metres or
    feet.
    """
    class Meta:
        name = "semiMajorAxis"
        namespace = "http://www.opengis.net/gml"


@dataclass
class SemiMinorAxis(MeasureType):
    """Length of the semi-minor axis of the ellipsoid.

    Uses the MeasureType with the restriction that the unit of measure
    referenced by uom must be suitable for a length, such as metres or
    feet.
    """
    class Meta:
        name = "semiMinorAxis"
        namespace = "http://www.opengis.net/gml"


@dataclass
class AbstractDatumBaseType:
    """
    Basic encoding for datum objects, simplifying and restricting the
    DefinitionType as needed.
    """
    meta_data_property: List[MetaDataProperty] = field(
        default_factory=list,
        metadata={
            "name": "metaDataProperty",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    description: Optional[Description] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    group_name: List[GroupName] = field(
        default_factory=list,
        metadata={
            "name": "groupName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    parameter_name: List[ParameterName] = field(
        default_factory=list,
        metadata={
            "name": "parameterName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    method_name: List[MethodName] = field(
        default_factory=list,
        metadata={
            "name": "methodName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    coordinate_operation_name: List[CoordinateOperationName] = field(
        default_factory=list,
        metadata={
            "name": "coordinateOperationName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    ellipsoid_name: List[EllipsoidName] = field(
        default_factory=list,
        metadata={
            "name": "ellipsoidName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    meridian_name: List[MeridianName] = field(
        default_factory=list,
        metadata={
            "name": "meridianName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    datum_name: Optional[DatumName] = field(
        default=None,
        metadata={
            "name": "datumName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    cs_name: List[CsName] = field(
        default_factory=list,
        metadata={
            "name": "csName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    srs_name: List[SrsName] = field(
        default_factory=list,
        metadata={
            "name": "srsName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    name: List[Name] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )


@dataclass
class EllipsoidBaseType:
    """
    Basic encoding for ellipsoid objects, simplifying and restricting the
    DefinitionType as needed.
    """
    meta_data_property: List[MetaDataProperty] = field(
        default_factory=list,
        metadata={
            "name": "metaDataProperty",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    description: Optional[Description] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    group_name: List[GroupName] = field(
        default_factory=list,
        metadata={
            "name": "groupName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    parameter_name: List[ParameterName] = field(
        default_factory=list,
        metadata={
            "name": "parameterName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    method_name: List[MethodName] = field(
        default_factory=list,
        metadata={
            "name": "methodName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    coordinate_operation_name: List[CoordinateOperationName] = field(
        default_factory=list,
        metadata={
            "name": "coordinateOperationName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    ellipsoid_name: Optional[EllipsoidName] = field(
        default=None,
        metadata={
            "name": "ellipsoidName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    meridian_name: List[MeridianName] = field(
        default_factory=list,
        metadata={
            "name": "meridianName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    datum_name: List[DatumName] = field(
        default_factory=list,
        metadata={
            "name": "datumName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    cs_name: List[CsName] = field(
        default_factory=list,
        metadata={
            "name": "csName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    srs_name: List[SrsName] = field(
        default_factory=list,
        metadata={
            "name": "srsName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    name: List[Name] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )


@dataclass
class PrimeMeridianBaseType:
    """
    Basic encoding for prime meridian objects, simplifying and restricting the
    DefinitionType as needed.
    """
    meta_data_property: List[MetaDataProperty] = field(
        default_factory=list,
        metadata={
            "name": "metaDataProperty",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    description: Optional[Description] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    group_name: List[GroupName] = field(
        default_factory=list,
        metadata={
            "name": "groupName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    parameter_name: List[ParameterName] = field(
        default_factory=list,
        metadata={
            "name": "parameterName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    method_name: List[MethodName] = field(
        default_factory=list,
        metadata={
            "name": "methodName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    coordinate_operation_name: List[CoordinateOperationName] = field(
        default_factory=list,
        metadata={
            "name": "coordinateOperationName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    ellipsoid_name: List[EllipsoidName] = field(
        default_factory=list,
        metadata={
            "name": "ellipsoidName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    meridian_name: Optional[MeridianName] = field(
        default=None,
        metadata={
            "name": "meridianName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    datum_name: List[DatumName] = field(
        default_factory=list,
        metadata={
            "name": "datumName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    cs_name: List[CsName] = field(
        default_factory=list,
        metadata={
            "name": "csName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    srs_name: List[SrsName] = field(
        default_factory=list,
        metadata={
            "name": "srsName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    name: List[Name] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )


@dataclass
class SecondDefiningParameterType:
    """Definition of the second parameter that defines the shape of an
    ellipsoid.

    An ellipsoid requires two defining parameters: semi-major axis and
    inverse flattening or semi-major axis and semi-minor axis. When the
    reference body is a sphere rather than an ellipsoid, only a single
    defining parameter is required, namely the radius of the sphere; in
    that case, the semi-major axis "degenerates" into the radius of the
    sphere.
    """
    inverse_flattening: Optional[InverseFlattening] = field(
        default=None,
        metadata={
            "name": "inverseFlattening",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    semi_minor_axis: Optional[SemiMinorAxis] = field(
        default=None,
        metadata={
            "name": "semiMinorAxis",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    is_sphere: Optional[IsSphereValue] = field(
        default=None,
        metadata={
            "name": "isSphere",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class PixelInCell(PixelInCellType):
    class Meta:
        name = "pixelInCell"
        namespace = "http://www.opengis.net/gml"


@dataclass
class VerticalDatumType(VerticalDatumTypeType):
    class Meta:
        name = "verticalDatumType"
        namespace = "http://www.opengis.net/gml"


@dataclass
class AbstractDatumType(AbstractDatumBaseType):
    """A datum specifies the relationship of a coordinate system to the earth,
    thus creating a coordinate reference system.

    A datum uses a parameter or set of parameters that determine the
    location of the origin of the coordinate reference system. Each
    datum subtype can be associated with only specific types of
    coordinate systems. This abstract complexType shall not be used,
    extended, or restricted, in an Application Schema, to define a
    concrete subtype with a meaning equivalent to a concrete subtype
    specified in this document.

    :ivar datum_id: Set of alternative identifications of this datum.
        The first datumID, if any, is normally the primary
        identification code, and any others are aliases.
    :ivar remarks: Comments on this reference system, including source
        information.
    :ivar anchor_point:
    :ivar realization_epoch:
    :ivar valid_area:
    :ivar scope:
    """
    datum_id: List[DatumId] = field(
        default_factory=list,
        metadata={
            "name": "datumID",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    remarks: Optional[Remarks] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    anchor_point: Optional[AnchorPoint] = field(
        default=None,
        metadata={
            "name": "anchorPoint",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    realization_epoch: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "realizationEpoch",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    valid_area: Optional[ValidArea] = field(
        default=None,
        metadata={
            "name": "validArea",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    scope: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class PrimeMeridianType(PrimeMeridianBaseType):
    """
    A prime meridian defines the origin from which longitude values are
    determined.

    :ivar meridian_id: Set of alternative identifications of this prime
        meridian. The first meridianID, if any, is normally the primary
        identification code, and any others are aliases.
    :ivar remarks: Comments on or information about this prime meridian,
        including source information.
    :ivar greenwich_longitude:
    """
    meridian_id: List[MeridianId] = field(
        default_factory=list,
        metadata={
            "name": "meridianID",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    remarks: Optional[Remarks] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    greenwich_longitude: Optional[GreenwichLongitude] = field(
        default=None,
        metadata={
            "name": "greenwichLongitude",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )


@dataclass
class SecondDefiningParameter(SecondDefiningParameterType):
    class Meta:
        name = "secondDefiningParameter"
        namespace = "http://www.opengis.net/gml"


@dataclass
class EllipsoidType(EllipsoidBaseType):
    """An ellipsoid is a geometric figure that can be used to describe the
    approximate shape of the earth.

    In mathematical terms, it is a surface formed by the rotation of an
    ellipse about its minor axis.

    :ivar ellipsoid_id: Set of alternative identifications of this
        ellipsoid. The first ellipsoidID, if any, is normally the
        primary identification code, and any others are aliases.
    :ivar remarks: Comments on or information about this ellipsoid,
        including source information.
    :ivar semi_major_axis:
    :ivar second_defining_parameter:
    """
    ellipsoid_id: List[EllipsoidId] = field(
        default_factory=list,
        metadata={
            "name": "ellipsoidID",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    remarks: Optional[Remarks] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    semi_major_axis: Optional[SemiMajorAxis] = field(
        default=None,
        metadata={
            "name": "semiMajorAxis",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    second_defining_parameter: Optional[SecondDefiningParameter] = field(
        default=None,
        metadata={
            "name": "secondDefiningParameter",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )


@dataclass
class EngineeringDatumType(AbstractDatumType):
    """An engineering datum defines the origin of an engineering coordinate
    reference system, and is used in a region around that origin.

    This origin can be fixed with respect to the earth (such as a
    defined point at a construction site), or be a defined point on a
    moving vehicle (such as on a ship or satellite).
    """


@dataclass
class ImageDatumType(AbstractDatumType):
    """An image datum defines the origin of an image coordinate reference
    system, and is used in a local context only.

    For more information, see OGC Abstract Specification Topic 2.
    """
    pixel_in_cell: Optional[PixelInCell] = field(
        default=None,
        metadata={
            "name": "pixelInCell",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )


@dataclass
class PrimeMeridian(PrimeMeridianType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class TemporalDatumBaseType(AbstractDatumType):
    """Partially defines the origin of a temporal coordinate reference system.

    This type restricts the AbstractDatumType to remove the
    "anchorPoint" and "realizationEpoch" elements.
    """


@dataclass
class VerticalDatumType1(AbstractDatumType):
    """A textual description and/or a set of parameters identifying a
    particular reference level surface used as a zero-height surface, including
    its position with respect to the Earth for any of the height types
    recognized by this standard.

    There are several types of Vertical Datums, and each may place
    constraints on the Coordinate Axis with which it is combined to
    create a Vertical CRS.
    """
    class Meta:
        name = "VerticalDatumType"

    vertical_datum_type: Optional[VerticalDatumType] = field(
        default=None,
        metadata={
            "name": "verticalDatumType",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class Datum(AbstractDatumType):
    class Meta:
        name = "_Datum"
        namespace = "http://www.opengis.net/gml"


@dataclass
class Ellipsoid(EllipsoidType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class EngineeringDatum(EngineeringDatumType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class ImageDatum(ImageDatumType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class PrimeMeridianRefType:
    """
    Association to a prime meridian, either referencing or containing the
    definition of that meridian.
    """
    prime_meridian: Optional[PrimeMeridian] = field(
        default=None,
        metadata={
            "name": "PrimeMeridian",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
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
    remote_schema: Optional[str] = field(
        default=None,
        metadata={
            "name": "remoteSchema",
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class TemporalDatumType(TemporalDatumBaseType):
    """Defines the origin of a temporal coordinate reference system.

    This type extends the TemporalDatumRestrictionType to add the
    "origin" element with the dateTime type.
    """
    origin: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )


@dataclass
class VerticalDatum(VerticalDatumType1):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class EllipsoidRefType:
    """
    Association to an ellipsoid, either referencing or containing the
    definition of that ellipsoid.
    """
    ellipsoid: Optional[Ellipsoid] = field(
        default=None,
        metadata={
            "name": "Ellipsoid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
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
    remote_schema: Optional[str] = field(
        default=None,
        metadata={
            "name": "remoteSchema",
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class EngineeringDatumRefType:
    """
    Association to an engineering datum, either referencing or containing the
    definition of that datum.
    """
    engineering_datum: Optional[EngineeringDatum] = field(
        default=None,
        metadata={
            "name": "EngineeringDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
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
    remote_schema: Optional[str] = field(
        default=None,
        metadata={
            "name": "remoteSchema",
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class ImageDatumRefType:
    """
    Association to an image datum, either referencing or containing the
    definition of that datum.
    """
    image_datum: Optional[ImageDatum] = field(
        default=None,
        metadata={
            "name": "ImageDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
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
    remote_schema: Optional[str] = field(
        default=None,
        metadata={
            "name": "remoteSchema",
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class TemporalDatum(TemporalDatumType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class VerticalDatumRefType:
    """
    Association to a vertical datum, either referencing or containing the
    definition of that datum.
    """
    vertical_datum: Optional[VerticalDatum] = field(
        default=None,
        metadata={
            "name": "VerticalDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
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
    remote_schema: Optional[str] = field(
        default=None,
        metadata={
            "name": "remoteSchema",
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class PrimeMeridianRef(PrimeMeridianRefType):
    class Meta:
        name = "primeMeridianRef"
        namespace = "http://www.opengis.net/gml"


@dataclass
class UsesPrimeMeridian(PrimeMeridianRefType):
    """
    Association to the prime meridian used by this geodetic datum.
    """
    class Meta:
        name = "usesPrimeMeridian"
        namespace = "http://www.opengis.net/gml"


@dataclass
class TemporalDatumRefType:
    """
    Association to a temporal datum, either referencing or containing the
    definition of that datum.
    """
    temporal_datum: Optional[TemporalDatum] = field(
        default=None,
        metadata={
            "name": "TemporalDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
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
    remote_schema: Optional[str] = field(
        default=None,
        metadata={
            "name": "remoteSchema",
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class EllipsoidRef(EllipsoidRefType):
    class Meta:
        name = "ellipsoidRef"
        namespace = "http://www.opengis.net/gml"


@dataclass
class EngineeringDatumRef(EngineeringDatumRefType):
    class Meta:
        name = "engineeringDatumRef"
        namespace = "http://www.opengis.net/gml"


@dataclass
class ImageDatumRef(ImageDatumRefType):
    class Meta:
        name = "imageDatumRef"
        namespace = "http://www.opengis.net/gml"


@dataclass
class UsesEllipsoid(EllipsoidRefType):
    """
    Association to the ellipsoid used by this geodetic datum.
    """
    class Meta:
        name = "usesEllipsoid"
        namespace = "http://www.opengis.net/gml"


@dataclass
class VerticalDatumRef(VerticalDatumRefType):
    class Meta:
        name = "verticalDatumRef"
        namespace = "http://www.opengis.net/gml"


@dataclass
class GeodeticDatumType(AbstractDatumType):
    """
    A geodetic datum defines the precise location and orientation in
    3-dimensional space of a defined ellipsoid (or sphere) that approximates
    the shape of the earth, or of a Cartesian coordinate system centered in
    this ellipsoid (or sphere).
    """
    uses_prime_meridian: Optional[UsesPrimeMeridian] = field(
        default=None,
        metadata={
            "name": "usesPrimeMeridian",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    uses_ellipsoid: Optional[UsesEllipsoid] = field(
        default=None,
        metadata={
            "name": "usesEllipsoid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )


@dataclass
class TemporalDatumRef(TemporalDatumRefType):
    class Meta:
        name = "temporalDatumRef"
        namespace = "http://www.opengis.net/gml"


@dataclass
class GeodeticDatum(GeodeticDatumType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class DatumRefType:
    """
    Association to a datum, either referencing or containing the definition of
    that datum.
    """
    geodetic_datum: Optional[GeodeticDatum] = field(
        default=None,
        metadata={
            "name": "GeodeticDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    temporal_datum: Optional[TemporalDatum] = field(
        default=None,
        metadata={
            "name": "TemporalDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    vertical_datum: Optional[VerticalDatum] = field(
        default=None,
        metadata={
            "name": "VerticalDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    image_datum: Optional[ImageDatum] = field(
        default=None,
        metadata={
            "name": "ImageDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    engineering_datum: Optional[EngineeringDatum] = field(
        default=None,
        metadata={
            "name": "EngineeringDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    datum: Optional[Datum] = field(
        default=None,
        metadata={
            "name": "_Datum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
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
    remote_schema: Optional[str] = field(
        default=None,
        metadata={
            "name": "remoteSchema",
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class GeodeticDatumRefType:
    """
    Association to a geodetic datum, either referencing or containing the
    definition of that datum.
    """
    geodetic_datum: Optional[GeodeticDatum] = field(
        default=None,
        metadata={
            "name": "GeodeticDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
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
    remote_schema: Optional[str] = field(
        default=None,
        metadata={
            "name": "remoteSchema",
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class DatumRef(DatumRefType):
    class Meta:
        name = "datumRef"
        namespace = "http://www.opengis.net/gml"


@dataclass
class GeodeticDatumRef(GeodeticDatumRefType):
    class Meta:
        name = "geodeticDatumRef"
        namespace = "http://www.opengis.net/gml"
