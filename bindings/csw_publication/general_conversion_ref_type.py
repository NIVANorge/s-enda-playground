from dataclasses import dataclass, field
from typing import List, Optional
from bindings.csw_publication.absolute_external_positional_accuracy import AbsoluteExternalPositionalAccuracy
from bindings.csw_publication.abstract_coordinate_operation_base_type import AbstractCoordinateOperationBaseType
from bindings.csw_publication.abstract_reference_system_type import AbstractReferenceSystemType
from bindings.csw_publication.actuate_type import ActuateType
from bindings.csw_publication.coordinate_operation_id import CoordinateOperationId
from bindings.csw_publication.coordinate_reference_system import CoordinateReferenceSystem
from bindings.csw_publication.covariance_matrix import CovarianceMatrix
from bindings.csw_publication.crs import Crs
from bindings.csw_publication.derived_crstype import DerivedCrstype
from bindings.csw_publication.engineering_crs import EngineeringCrs
from bindings.csw_publication.geocentric_crs import GeocentricCrs
from bindings.csw_publication.geographic_crs import GeographicCrs
from bindings.csw_publication.image_crs import ImageCrs
from bindings.csw_publication.positional_accuracy import PositionalAccuracy
from bindings.csw_publication.relative_internal_positional_accuracy import RelativeInternalPositionalAccuracy
from bindings.csw_publication.remarks import Remarks
from bindings.csw_publication.show_type import ShowType
from bindings.csw_publication.temporal_crs import TemporalCrs
from bindings.csw_publication.type_type import TypeType
from bindings.csw_publication.uses_cartesian_cs import UsesCartesianCs
from bindings.csw_publication.uses_cs import UsesCs
from bindings.csw_publication.uses_method import UsesMethod
from bindings.csw_publication.uses_value import UsesValue
from bindings.csw_publication.valid_area import ValidArea
from bindings.csw_publication.vertical_crs import VerticalCrs

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GeneralConversionRefType:
    """
    Association to a general conversion, either referencing or containing the
    definition of that conversion.
    """
    conversion: Optional["Conversion"] = field(
        default=None,
        metadata={
            "name": "Conversion",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    general_conversion: Optional["GeneralConversion"] = field(
        default=None,
        metadata={
            "name": "_GeneralConversion",
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
class DefinedByConversion(GeneralConversionRefType):
    """
    Association to the coordinate conversion used to define this derived CRS.
    """
    class Meta:
        name = "definedByConversion"
        namespace = "http://www.opengis.net/gml"


@dataclass
class AbstractGeneralDerivedCrstype(AbstractReferenceSystemType):
    """A coordinate reference system that is defined by its coordinate
    conversion from another coordinate reference system (not by a datum).

    This abstract complexType shall not be used, extended, or
    restricted, in an Application Schema, to define a concrete subtype
    with a meaning equivalent to a concrete subtype specified in this
    document.
    """
    class Meta:
        name = "AbstractGeneralDerivedCRSType"

    base_crs: Optional["BaseCrs"] = field(
        default=None,
        metadata={
            "name": "baseCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    defined_by_conversion: Optional[DefinedByConversion] = field(
        default=None,
        metadata={
            "name": "definedByConversion",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )


@dataclass
class DerivedCrstype1(AbstractGeneralDerivedCrstype):
    """A coordinate reference system that is defined by its coordinate
    conversion from another coordinate reference system but is not a projected
    coordinate reference system.

    This category includes coordinate reference systems derived from a
    projected coordinate reference system.
    """
    class Meta:
        name = "DerivedCRSType"

    derived_crstype: Optional[DerivedCrstype] = field(
        default=None,
        metadata={
            "name": "derivedCRSType",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    uses_cs: Optional[UsesCs] = field(
        default=None,
        metadata={
            "name": "usesCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )


@dataclass
class ProjectedCrstype(AbstractGeneralDerivedCrstype):
    """A 2D coordinate reference system used to approximate the shape of the
    earth on a planar surface, but in such a way that the distortion that is
    inherent to the approximation is carefully controlled and known.

    Distortion correction is commonly applied to calculated bearings and
    distances to produce values that are a close match to actual field
    values.
    """
    class Meta:
        name = "ProjectedCRSType"

    uses_cartesian_cs: Optional[UsesCartesianCs] = field(
        default=None,
        metadata={
            "name": "usesCartesianCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )


@dataclass
class GeneralDerivedCrs(AbstractGeneralDerivedCrstype):
    class Meta:
        name = "_GeneralDerivedCRS"
        namespace = "http://www.opengis.net/gml"


@dataclass
class DerivedCrs(DerivedCrstype1):
    class Meta:
        name = "DerivedCRS"
        namespace = "http://www.opengis.net/gml"


@dataclass
class ProjectedCrs(ProjectedCrstype):
    class Meta:
        name = "ProjectedCRS"
        namespace = "http://www.opengis.net/gml"


@dataclass
class CoordinateReferenceSystemRefType:
    """
    Association to a coordinate reference system, either referencing or
    containing the definition of that reference system.
    """
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
class BaseCrs(CoordinateReferenceSystemRefType):
    """
    Association to the coordinate reference system used by this derived CRS.
    """
    class Meta:
        name = "baseCRS"
        namespace = "http://www.opengis.net/gml"


@dataclass
class IncludesCrs(CoordinateReferenceSystemRefType):
    """
    An association to a component coordinate reference system included in this
    compound coordinate reference system.
    """
    class Meta:
        name = "includesCRS"
        namespace = "http://www.opengis.net/gml"


@dataclass
class CompoundCrstype(AbstractReferenceSystemType):
    """
    A coordinate reference system describing the position of points through two
    or more independent coordinate reference systems.

    :ivar includes_crs: Ordered sequence of associations to all the
        component coordinate reference systems included in this compound
        coordinate reference system.
    """
    class Meta:
        name = "CompoundCRSType"

    includes_crs: List[IncludesCrs] = field(
        default_factory=list,
        metadata={
            "name": "includesCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 2,
        }
    )


@dataclass
class CompoundCrs(CompoundCrstype):
    class Meta:
        name = "CompoundCRS"
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
class SourceCrs(CrsrefType):
    """
    Association to the source CRS (coordinate reference system) of this
    coordinate operation.
    """
    class Meta:
        name = "sourceCRS"
        namespace = "http://www.opengis.net/gml"


@dataclass
class TargetCrs(CrsrefType):
    """Association to the target CRS (coordinate reference system) of this
    coordinate operation.

    For constraints on multiplicity of "sourceCRS" and "targetCRS", see
    UML model of Coordinate Operation package in OGC Abstract
    Specification topic 2.
    """
    class Meta:
        name = "targetCRS"
        namespace = "http://www.opengis.net/gml"


@dataclass
class AbstractCoordinateOperationType(AbstractCoordinateOperationBaseType):
    """A mathematical operation on coordinates that transforms or converts
    coordinates to another coordinate reference system.

    Many but not all coordinate operations (from CRS A to CRS B) also
    uniquely define the inverse operation (from CRS B to CRS A). In some
    cases, the operation method algorithm for the inverse operation is
    the same as for the forward algorithm, but the signs of some
    operation parameter values must be reversed. In other cases,
    different algorithms are required for the forward and inverse
    operations, but the same operation parameter values are used. If
    (some) entirely different parameter values are needed, a different
    coordinate operation shall be defined.

    :ivar coordinate_operation_id: Set of alternative identifications of
        this coordinate operation. The first coordinateOperationID, if
        any, is normally the primary identification code, and any others
        are aliases.
    :ivar remarks: Comments on or information about this coordinate
        operation, including source information.
    :ivar operation_version:
    :ivar valid_area:
    :ivar scope:
    :ivar covariance_matrix:
    :ivar relative_internal_positional_accuracy:
    :ivar absolute_external_positional_accuracy:
    :ivar positional_accuracy: Unordered set of estimates of the impact
        of this coordinate operation on point position accuracy. Gives
        position error estimates for target coordinates of this
        coordinate operation, assuming no errors in source coordinates.
    :ivar source_crs:
    :ivar target_crs:
    """
    coordinate_operation_id: List[CoordinateOperationId] = field(
        default_factory=list,
        metadata={
            "name": "coordinateOperationID",
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
    operation_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "operationVersion",
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
    covariance_matrix: List[CovarianceMatrix] = field(
        default_factory=list,
        metadata={
            "name": "covarianceMatrix",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    relative_internal_positional_accuracy: List[RelativeInternalPositionalAccuracy] = field(
        default_factory=list,
        metadata={
            "name": "relativeInternalPositionalAccuracy",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    absolute_external_positional_accuracy: List[AbsoluteExternalPositionalAccuracy] = field(
        default_factory=list,
        metadata={
            "name": "absoluteExternalPositionalAccuracy",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    positional_accuracy: List[PositionalAccuracy] = field(
        default_factory=list,
        metadata={
            "name": "_positionalAccuracy",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    source_crs: Optional[SourceCrs] = field(
        default=None,
        metadata={
            "name": "sourceCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    target_crs: Optional[TargetCrs] = field(
        default=None,
        metadata={
            "name": "targetCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class AbstractGeneralConversionType(AbstractCoordinateOperationType):
    """An abstract operation on coordinates that does not include any change of
    datum.

    The best-known example of a coordinate conversion is a map
    projection. The parameters describing coordinate conversions are
    defined rather than empirically derived. Note that some conversions
    have no parameters. This abstract complexType is expected to be
    extended for well-known operation methods with many Conversion
    instances, in Application Schemas that define operation-method-
    specialized element names and contents. This conversion uses an
    operation method, usually with associated parameter values. However,
    operation methods and parameter values are directly associated with
    concrete subtypes, not with this abstract type. All concrete types
    derived from this type shall extend this type to include a
    "usesMethod" element that references the "OperationMethod" element.
    Similarly, all concrete types derived from this type shall extend
    this type to include zero or more elements each named "uses...Value"
    that each use the type of an element substitutable for the
    "_generalParameterValue" element.
    """


@dataclass
class ConversionType(AbstractGeneralConversionType):
    """A concrete operation on coordinates that does not include any change of
    Datum.

    The best-known example of a coordinate conversion is a map
    projection. The parameters describing coordinate conversions are
    defined rather than empirically derived. Note that some conversions
    have no parameters. This concrete complexType can be used with all
    operation methods, without using an Application Schema that defines
    operation-method-specialized element names and contents, especially
    for methods with only one Conversion instance.

    :ivar uses_method:
    :ivar uses_value: Unordered list of composition associations to the
        set of parameter values used by this conversion operation.
    """
    uses_method: Optional[UsesMethod] = field(
        default=None,
        metadata={
            "name": "usesMethod",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    uses_value: List[UsesValue] = field(
        default_factory=list,
        metadata={
            "name": "usesValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class GeneralConversion(AbstractGeneralConversionType):
    class Meta:
        name = "_GeneralConversion"
        namespace = "http://www.opengis.net/gml"


@dataclass
class Conversion(ConversionType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
