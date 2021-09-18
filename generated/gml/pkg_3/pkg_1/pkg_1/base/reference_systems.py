from dataclasses import dataclass, field
from typing import List, Optional
from generated.gml.pkg_3.pkg_1.pkg_1.base.basic_types import CodeType
from generated.gml.pkg_3.pkg_1.pkg_1.base.coordinate_operations import (
    CoordinateOperationName,
    GroupName,
    MethodName,
    ParameterName,
)
from generated.gml.pkg_3.pkg_1.pkg_1.base.coordinate_reference_systems import (
    CompoundCrs,
    DerivedCrs,
    EngineeringCrs,
    GeocentricCrs,
    GeographicCrs,
    ImageCrs,
    ProjectedCrs,
    TemporalCrs,
    VerticalCrs,
    CoordinateReferenceSystem,
    GeneralDerivedCrs,
)
from generated.gml.pkg_3.pkg_1.pkg_1.base.coordinate_systems import CsName
from generated.gml.pkg_3.pkg_1.pkg_1.base.datums import (
    DatumName,
    EllipsoidName,
    MeridianName,
)
from generated.gml.pkg_3.pkg_1.pkg_1.base.geometry_basic0d1d import EnvelopeType
from generated.gml.pkg_3.pkg_1.pkg_1.base.geometry_basic2d import PolygonType
from generated.gml.pkg_3.pkg_1.pkg_1.base.gml_base import (
    StringOrRefType,
    Description,
    MetaDataProperty,
    Name,
)
from generated.gml.pkg_3.pkg_1.pkg_1.base.temporal import TimePeriodType
from generated.xlink import (
    ActuateType,
    ShowType,
    TypeType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Scope:
    """
    Description of domain of usage, or limitations of usage, for which this CRS
    object is valid.
    """
    class Meta:
        name = "scope"
        namespace = "http://www.opengis.net/gml"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class Version:
    """Identifier of the version of the associated codeSpace or code, as
    specified by the codeSpace or code authority.

    This version is included only when the "code" or "codeSpace" uses
    versions. When appropriate, the version is identified by the
    effective date, coded using ISO 8601 date format.
    """
    class Meta:
        name = "version"
        namespace = "http://www.opengis.net/gml"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class BoundingBox(EnvelopeType):
    """
    A bounding box (or envelope) defining the spatial domain of this object.
    """
    class Meta:
        name = "boundingBox"
        namespace = "http://www.opengis.net/gml"


@dataclass
class BoundingPolygon(PolygonType):
    """
    A bounding polygon defining the horizontal spatial domain of this object.
    """
    class Meta:
        name = "boundingPolygon"
        namespace = "http://www.opengis.net/gml"


@dataclass
class Remarks(StringOrRefType):
    """Information about this object or code.

    Contains text or refers to external text.
    """
    class Meta:
        name = "remarks"
        namespace = "http://www.opengis.net/gml"


@dataclass
class SrsName(CodeType):
    """
    The name by which this reference system is identified.
    """
    class Meta:
        name = "srsName"
        namespace = "http://www.opengis.net/gml"


@dataclass
class TemporalExtent(TimePeriodType):
    """
    A time period defining the temporal domain of this object.
    """
    class Meta:
        name = "temporalExtent"
        namespace = "http://www.opengis.net/gml"


@dataclass
class VerticalExtent(EnvelopeType):
    """
    An interval defining the vertical spatial domain of this object.
    """
    class Meta:
        name = "verticalExtent"
        namespace = "http://www.opengis.net/gml"


@dataclass
class AbstractReferenceSystemBaseType:
    """
    Basic encoding for reference system objects, simplifying and restricting
    the DefinitionType as needed.
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
    srs_name: Optional[SrsName] = field(
        default=None,
        metadata={
            "name": "srsName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
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
    description: Optional[Description] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    bounding_box: List[BoundingBox] = field(
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


@dataclass
class IdentifierType:
    """An identification of a CRS object.

    The first use of the IdentifierType for an object, if any, is
    normally the primary identification code, and any others are
    aliases.

    :ivar group_name:
    :ivar parameter_name:
    :ivar method_name:
    :ivar coordinate_operation_name:
    :ivar ellipsoid_name:
    :ivar meridian_name:
    :ivar datum_name:
    :ivar cs_name:
    :ivar srs_name:
    :ivar name: The code or name for this Identifier, often from a
        controlled list or pattern defined by a code space. The optional
        codeSpace attribute is normally included to identify or
        reference a code space within which one or more codes are
        defined. This code space is often defined by some authority
        organization, where one organization may define multiple code
        spaces. The range and format of each Code Space identifier is
        defined by that code space authority. Information about that
        code space authority can be included as metaDataProperty
        elements which are optionally allowed in all CRS objects.
    :ivar version:
    :ivar remarks: Remarks about this code or alias.
    """
    group_name: Optional[GroupName] = field(
        default=None,
        metadata={
            "name": "groupName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    parameter_name: Optional[ParameterName] = field(
        default=None,
        metadata={
            "name": "parameterName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    method_name: Optional[MethodName] = field(
        default=None,
        metadata={
            "name": "methodName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    coordinate_operation_name: Optional[CoordinateOperationName] = field(
        default=None,
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
        }
    )
    meridian_name: Optional[MeridianName] = field(
        default=None,
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
        }
    )
    cs_name: Optional[CsName] = field(
        default=None,
        metadata={
            "name": "csName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    srs_name: Optional[SrsName] = field(
        default=None,
        metadata={
            "name": "srsName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    name: Optional[Name] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    version: Optional[str] = field(
        default=None,
        metadata={
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


@dataclass
class SrsId(IdentifierType):
    """
    An identification of a reference system.
    """
    class Meta:
        name = "srsID"
        namespace = "http://www.opengis.net/gml"


@dataclass
class ValidArea(ExtentType):
    """
    Area or region in which this CRS object is valid.
    """
    class Meta:
        name = "validArea"
        namespace = "http://www.opengis.net/gml"


@dataclass
class AbstractReferenceSystemType(AbstractReferenceSystemBaseType):
    """
    Description of a spatial and/or temporal reference system used by a
    dataset.

    :ivar srs_id: Set of alterative identifications of this reference
        system. The first srsID, if any, is normally the primary
        identification code, and any others are aliases.
    :ivar remarks: Comments on or information about this reference
        system, including source information.
    :ivar valid_area:
    :ivar scope:
    """
    srs_id: List[SrsId] = field(
        default_factory=list,
        metadata={
            "name": "srsID",
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
class Crs(AbstractReferenceSystemType):
    """Abstract coordinate reference system, usually defined by a coordinate
    system and a datum.

    This abstract complexType shall not be used, extended, or
    restricted, in an Application Schema, to define a concrete subtype
    with a meaning equivalent to a concrete subtype specified in this
    document.
    """
    class Meta:
        name = "_CRS"
        namespace = "http://www.opengis.net/gml"


@dataclass
class ReferenceSystem(AbstractReferenceSystemType):
    class Meta:
        name = "_ReferenceSystem"
        namespace = "http://www.opengis.net/gml"


@dataclass
class CrsrefType:
    """
    Association to a CRS abstract coordinate reference system, either
    referencing or containing the definition of that CRS.
    """
    class Meta:
        name = "CRSRefType"

    compound_crs: Optional[CompoundCrs] = field(
        default=None,
        metadata={
            "name": "CompoundCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    temporal_crs: Optional[TemporalCrs] = field(
        default=None,
        metadata={
            "name": "TemporalCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    image_crs: Optional[ImageCrs] = field(
        default=None,
        metadata={
            "name": "ImageCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    engineering_crs: Optional[EngineeringCrs] = field(
        default=None,
        metadata={
            "name": "EngineeringCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    derived_crs: Optional[DerivedCrs] = field(
        default=None,
        metadata={
            "name": "DerivedCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    projected_crs: Optional[ProjectedCrs] = field(
        default=None,
        metadata={
            "name": "ProjectedCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    general_derived_crs: Optional[GeneralDerivedCrs] = field(
        default=None,
        metadata={
            "name": "_GeneralDerivedCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    geocentric_crs: Optional[GeocentricCrs] = field(
        default=None,
        metadata={
            "name": "GeocentricCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    vertical_crs: Optional[VerticalCrs] = field(
        default=None,
        metadata={
            "name": "VerticalCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    geographic_crs: Optional[GeographicCrs] = field(
        default=None,
        metadata={
            "name": "GeographicCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    coordinate_reference_system: Optional[CoordinateReferenceSystem] = field(
        default=None,
        metadata={
            "name": "_CoordinateReferenceSystem",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    crs: Optional[Crs] = field(
        default=None,
        metadata={
            "name": "_CRS",
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
class ReferenceSystemRefType:
    """
    Association to a reference system, either referencing or containing the
    definition of that reference system.
    """
    compound_crs: Optional[CompoundCrs] = field(
        default=None,
        metadata={
            "name": "CompoundCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    temporal_crs: Optional[TemporalCrs] = field(
        default=None,
        metadata={
            "name": "TemporalCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    image_crs: Optional[ImageCrs] = field(
        default=None,
        metadata={
            "name": "ImageCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    engineering_crs: Optional[EngineeringCrs] = field(
        default=None,
        metadata={
            "name": "EngineeringCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    derived_crs: Optional[DerivedCrs] = field(
        default=None,
        metadata={
            "name": "DerivedCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    projected_crs: Optional[ProjectedCrs] = field(
        default=None,
        metadata={
            "name": "ProjectedCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    general_derived_crs: Optional[GeneralDerivedCrs] = field(
        default=None,
        metadata={
            "name": "_GeneralDerivedCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    geocentric_crs: Optional[GeocentricCrs] = field(
        default=None,
        metadata={
            "name": "GeocentricCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    vertical_crs: Optional[VerticalCrs] = field(
        default=None,
        metadata={
            "name": "VerticalCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    geographic_crs: Optional[GeographicCrs] = field(
        default=None,
        metadata={
            "name": "GeographicCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    coordinate_reference_system: Optional[CoordinateReferenceSystem] = field(
        default=None,
        metadata={
            "name": "_CoordinateReferenceSystem",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    crs: Optional[Crs] = field(
        default=None,
        metadata={
            "name": "_CRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    reference_system: Optional[ReferenceSystem] = field(
        default=None,
        metadata={
            "name": "_ReferenceSystem",
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
class CrsRef(CrsrefType):
    class Meta:
        name = "crsRef"
        namespace = "http://www.opengis.net/gml"


@dataclass
class ReferenceSystemRef(ReferenceSystemRefType):
    class Meta:
        name = "referenceSystemRef"
        namespace = "http://www.opengis.net/gml"
