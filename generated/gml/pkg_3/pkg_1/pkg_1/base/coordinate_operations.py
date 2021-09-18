from dataclasses import dataclass, field
from typing import List, Optional
from generated.gml.pkg_3.pkg_1.pkg_1.base.basic_types import (
    CodeType,
    MeasureListType,
    MeasureType,
)
from generated.gml.pkg_3.pkg_1.pkg_1.base.coordinate_systems import CsName
from generated.gml.pkg_3.pkg_1.pkg_1.base.data_quality import (
    PositionalAccuracy,
    AbsoluteExternalPositionalAccuracy,
    CovarianceMatrix,
    RelativeInternalPositionalAccuracy,
)
from generated.gml.pkg_3.pkg_1.pkg_1.base.datums import (
    DatumName,
    EllipsoidName,
    MeridianName,
)
from generated.gml.pkg_3.pkg_1.pkg_1.base.dictionary import DefinitionType
from generated.gml.pkg_3.pkg_1.pkg_1.base.gml_base import (
    Description,
    MetaDataProperty,
    Name,
)
from generated.gml.pkg_3.pkg_1.pkg_1.base.measures import DmsangleType
from generated.gml.pkg_3.pkg_1.pkg_1.base.reference_systems import (
    CrsrefType,
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


@dataclass
class AbstractGeneralParameterValueType:
    """Abstract parameter value or group of parameter values.

    This abstract complexType is expected to be extended and restricted
    for well-known operation methods with many instances, in Application
    Schemas that define operation-method-specialized element names and
    contents. Specific parameter value elements are directly contained
    in concrete subtypes, not in this abstract type. All concrete types
    derived from this type shall extend this type to include one
    "...Value" element with an appropriate type, which should be one of
    the element types allowed in the ParameterValueType. In addition,
    all derived concrete types shall extend this type to include a
    "valueOfParameter" element that references one element substitutable
    for the "OperationParameter" element.
    """


@dataclass
class BooleanValue:
    """Boolean value of an operation parameter.

    A Boolean value does not have an associated unit of measure.
    """
    class Meta:
        name = "booleanValue"
        namespace = "http://www.opengis.net/gml"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class IntegerValue:
    """Positive integer value of an operation parameter, usually used for a
    count.

    An integer value does not have an associated unit of measure.
    """
    class Meta:
        name = "integerValue"
        namespace = "http://www.opengis.net/gml"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class IntegerValueList:
    """Ordered sequence of two or more integer values of an operation parameter
    list, usually used for counts.

    These integer values do not have an associated unit of measure. An
    element of this type contains a space-separated sequence of integer
    values.
    """
    class Meta:
        name = "integerValueList"
        namespace = "http://www.opengis.net/gml"

    value: List[int] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        }
    )


@dataclass
class MaximumOccurs:
    """The maximum number of times that values for this parameter group can be
    included.

    If this attribute is omitted, the maximum number is one.
    """
    class Meta:
        name = "maximumOccurs"
        namespace = "http://www.opengis.net/gml"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class MinimumOccurs:
    """The minimum number of times that values for this parameter group or
    parameter are required.

    If this attribute is omitted, the minimum number is one.
    """
    class Meta:
        name = "minimumOccurs"
        namespace = "http://www.opengis.net/gml"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class ModifiedCoordinate:
    """
    A positive integer defining a position in a coordinate tuple.
    """
    class Meta:
        name = "modifiedCoordinate"
        namespace = "http://www.opengis.net/gml"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class OperationVersion:
    """Version of the coordinate transformation (i.e., instantiation due to the
    stochastic nature of the parameters).

    Mandatory when describing a transformation, and should not be
    supplied for a conversion.
    """
    class Meta:
        name = "operationVersion"
        namespace = "http://www.opengis.net/gml"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class SourceDimensions:
    """
    Number of dimensions in the source CRS of this operation method.
    """
    class Meta:
        name = "sourceDimensions"
        namespace = "http://www.opengis.net/gml"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class StringValue:
    """String value of an operation parameter.

    A string value does not have an associated unit of measure.
    """
    class Meta:
        name = "stringValue"
        namespace = "http://www.opengis.net/gml"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class TargetDimensions:
    """
    Number of dimensions in the target CRS of this operation method.
    """
    class Meta:
        name = "targetDimensions"
        namespace = "http://www.opengis.net/gml"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class ValueFile:
    """Reference to a file or a part of a file containing one or more parameter
    values, each numeric value with its associated unit of measure.

    When referencing a part of a file, that file must contain multiple
    identified parts, such as an XML encoded document. Furthermore, the
    referenced file or part of a file can reference another part of the
    same or different files, as allowed in XML documents.
    """
    class Meta:
        name = "valueFile"
        namespace = "http://www.opengis.net/gml"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class AbstractGeneralOperationParameterType(DefinitionType):
    """
    Abstract definition of a parameter or group of parameters used by an
    operation method.
    """
    minimum_occurs: Optional[int] = field(
        default=None,
        metadata={
            "name": "minimumOccurs",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


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
class GeneralParameterValue(AbstractGeneralParameterValueType):
    class Meta:
        name = "_generalParameterValue"
        namespace = "http://www.opengis.net/gml"


@dataclass
class CoordinateOperationId(IdentifierType):
    """
    An identification of a coordinate operation.
    """
    class Meta:
        name = "coordinateOperationID"
        namespace = "http://www.opengis.net/gml"


@dataclass
class CoordinateOperationName(CodeType):
    """
    The name by which this coordinate operation is identified.
    """
    class Meta:
        name = "coordinateOperationName"
        namespace = "http://www.opengis.net/gml"


@dataclass
class DmsAngleValue(DmsangleType):
    """
    Value of an angle operation parameter, in either degree-minute-second
    format or single value format.
    """
    class Meta:
        name = "dmsAngleValue"
        namespace = "http://www.opengis.net/gml"


@dataclass
class GroupId(IdentifierType):
    """
    An identification of an operation parameter group.
    """
    class Meta:
        name = "groupID"
        namespace = "http://www.opengis.net/gml"


@dataclass
class GroupName(CodeType):
    """
    The name by which this operation parameter group is identified.
    """
    class Meta:
        name = "groupName"
        namespace = "http://www.opengis.net/gml"


@dataclass
class IncludesValue(AbstractGeneralParameterValueType):
    """
    A composition association to a parameter value or group of values included
    in this group.
    """
    class Meta:
        name = "includesValue"
        namespace = "http://www.opengis.net/gml"


@dataclass
class MethodFormula(CodeType):
    """Formula(s) used by this operation method.

    The value may be a reference to a publication. Note that the
    operation method may not be analytic, in which case this element
    references or contains the procedure, not an analytic formula.
    """
    class Meta:
        name = "methodFormula"
        namespace = "http://www.opengis.net/gml"


@dataclass
class MethodId(IdentifierType):
    """
    An identification of an operation method.
    """
    class Meta:
        name = "methodID"
        namespace = "http://www.opengis.net/gml"


@dataclass
class MethodName(CodeType):
    """
    The name by which this operation method is identified.
    """
    class Meta:
        name = "methodName"
        namespace = "http://www.opengis.net/gml"


@dataclass
class ParameterId(IdentifierType):
    """
    An identification of an operation parameter.
    """
    class Meta:
        name = "parameterID"
        namespace = "http://www.opengis.net/gml"


@dataclass
class ParameterName(CodeType):
    """
    The name by which this operation parameter is identified.
    """
    class Meta:
        name = "parameterName"
        namespace = "http://www.opengis.net/gml"


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
class Value(MeasureType):
    """
    Numeric value of an operation parameter, with its associated unit of
    measure.
    """
    class Meta:
        name = "value"
        namespace = "http://www.opengis.net/gml"


@dataclass
class ValueList(MeasureListType):
    """Ordered sequence of two or more numeric values of an operation parameter
    list, where each value has the same associated unit of measure.

    An element of this type contains a space-separated sequence of
    double values.
    """
    class Meta:
        name = "valueList"
        namespace = "http://www.opengis.net/gml"


@dataclass
class AbstractCoordinateOperationBaseType:
    """
    Basic encoding for coordinate operation objects, simplifying and
    restricting the DefinitionType as needed.
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
    coordinate_operation_name: Optional[CoordinateOperationName] = field(
        default=None,
        metadata={
            "name": "coordinateOperationName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
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
class OperationMethodBaseType:
    """
    Basic encoding for operation method objects, simplifying and restricting
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
    method_name: Optional[MethodName] = field(
        default=None,
        metadata={
            "name": "methodName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
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
class OperationParameterBaseType(AbstractGeneralOperationParameterType):
    """
    Basic encoding for operation parameter objects, simplifying and restricting
    the DefinitionType as needed.
    """


@dataclass
class OperationParameterGroupBaseType(AbstractGeneralOperationParameterType):
    """
    Basic encoding for operation parameter group objects, simplifying and
    restricting the DefinitionType as needed.
    """


@dataclass
class GeneralOperationParameter(AbstractGeneralOperationParameterType):
    class Meta:
        name = "_GeneralOperationParameter"
        namespace = "http://www.opengis.net/gml"


@dataclass
class GeneralConversionRef(GeneralConversionRefType):
    class Meta:
        name = "generalConversionRef"
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
class OperationParameterType(OperationParameterBaseType):
    """The definition of a parameter used by an operation method.

    Most parameter values are numeric, but other types of parameter
    values are possible. This complexType is expected to be used or
    extended for all operation methods, without defining operation-
    method-specialized element names.

    :ivar parameter_id: Set of alternative identifications of this
        operation parameter. The first parameterID, if any, is normally
        the primary identification code, and any others are aliases.
    :ivar remarks: Comments on or information about this operation
        parameter, including source information.
    """
    parameter_id: List[ParameterId] = field(
        default_factory=list,
        metadata={
            "name": "parameterID",
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
class AbstractGeneralTransformationType(AbstractCoordinateOperationType):
    """An abstract operation on coordinates that usually includes a change of
    Datum.

    The parameters of a coordinate transformation are empirically
    derived from data containing the coordinates of a series of points
    in both coordinate reference systems. This computational process is
    usually "over-determined", allowing derivation of error (or
    accuracy) estimates for the transformation. Also, the stochastic
    nature of the parameters may result in multiple (different) versions
    of the same coordinate transformation. This abstract complexType is
    expected to be extended for well-known operation methods with many
    Transformation instances, in Application Schemas that define
    operation-method-specialized value element names and contents. This
    transformation uses an operation method with associated parameter
    values. However, operation methods and parameter values are directly
    associated with concrete subtypes, not with this abstract type. All
    concrete types derived from this type shall extend this type to
    include a "usesMethod" element that references one "OperationMethod"
    element. Similarly, all concrete types derived from this type shall
    extend this type to include one or more elements each named
    "uses...Value" that each use the type of an element substitutable
    for the "_generalParameterValue" element.
    """


@dataclass
class OperationParameter(OperationParameterType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class CoordinateOperation(AbstractCoordinateOperationType):
    class Meta:
        name = "_CoordinateOperation"
        namespace = "http://www.opengis.net/gml"


@dataclass
class Operation(AbstractCoordinateOperationType):
    """A parameterized mathematical operation on coordinates that transforms or
    converts coordinates to another coordinate reference system.

    This coordinate operation uses an operation method, usually with
    associated parameter values. However, operation methods and
    parameter values are directly associated with concrete subtypes, not
    with this abstract type. This abstract complexType shall not be
    directly used, extended, or restricted in a compliant Application
    Schema.
    """
    class Meta:
        name = "_Operation"
        namespace = "http://www.opengis.net/gml"


@dataclass
class SingleOperation(AbstractCoordinateOperationType):
    """
    A single (not concatenated) coordinate operation.
    """
    class Meta:
        name = "_SingleOperation"
        namespace = "http://www.opengis.net/gml"


@dataclass
class AbstractGeneralOperationParameterRefType:
    """
    Association to an operation parameter or group, either referencing or
    containing the definition of that parameter or group.
    """
    operation_parameter_group: Optional["OperationParameterGroup"] = field(
        default=None,
        metadata={
            "name": "OperationParameterGroup",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    operation_parameter: Optional[OperationParameter] = field(
        default=None,
        metadata={
            "name": "OperationParameter",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    general_operation_parameter: Optional[GeneralOperationParameter] = field(
        default=None,
        metadata={
            "name": "_GeneralOperationParameter",
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
class OperationParameterRefType:
    """
    Association to an operation parameter, either referencing or containing the
    definition of that parameter.
    """
    operation_parameter: Optional[OperationParameter] = field(
        default=None,
        metadata={
            "name": "OperationParameter",
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
class GeneralConversion(AbstractGeneralConversionType):
    class Meta:
        name = "_GeneralConversion"
        namespace = "http://www.opengis.net/gml"


@dataclass
class GeneralTransformation(AbstractGeneralTransformationType):
    class Meta:
        name = "_GeneralTransformation"
        namespace = "http://www.opengis.net/gml"


@dataclass
class AbstractGeneralOperationParameterRef(AbstractGeneralOperationParameterRefType):
    class Meta:
        name = "abstractGeneralOperationParameterRef"
        namespace = "http://www.opengis.net/gml"


@dataclass
class IncludesParameter(AbstractGeneralOperationParameterRefType):
    """
    Association to an operation parameter that is a member of a group.
    """
    class Meta:
        name = "includesParameter"
        namespace = "http://www.opengis.net/gml"


@dataclass
class OperationParameterGroupRef(OperationParameterRefType):
    class Meta:
        name = "operationParameterGroupRef"
        namespace = "http://www.opengis.net/gml"


@dataclass
class OperationParameterRef(OperationParameterRefType):
    class Meta:
        name = "operationParameterRef"
        namespace = "http://www.opengis.net/gml"


@dataclass
class UsesParameter(AbstractGeneralOperationParameterRefType):
    """
    Association to an operation parameter or parameter group used by this
    operation method.
    """
    class Meta:
        name = "usesParameter"
        namespace = "http://www.opengis.net/gml"


@dataclass
class ValueOfParameter(OperationParameterRefType):
    """
    Association to the operation parameter that this is a value of.
    """
    class Meta:
        name = "valueOfParameter"
        namespace = "http://www.opengis.net/gml"


@dataclass
class OperationMethodType(OperationMethodBaseType):
    """Definition of an algorithm used to perform a coordinate operation.

    Most operation methods use a number of operation parameters,
    although some coordinate conversions use none. Each coordinate
    operation using the method assigns values to these parameters.

    :ivar method_id: Set of alternative identifications of this
        operation method. The first methodID, if any, is normally the
        primary identification code, and any others are aliases.
    :ivar remarks: Comments on or information about this operation
        method, including source information.
    :ivar method_formula:
    :ivar source_dimensions:
    :ivar target_dimensions:
    :ivar uses_parameter: Unordered list of associations to the set of
        operation parameters and parameter groups used by this operation
        method.
    """
    method_id: List[MethodId] = field(
        default_factory=list,
        metadata={
            "name": "methodID",
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
    method_formula: Optional[MethodFormula] = field(
        default=None,
        metadata={
            "name": "methodFormula",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    source_dimensions: Optional[int] = field(
        default=None,
        metadata={
            "name": "sourceDimensions",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    target_dimensions: Optional[int] = field(
        default=None,
        metadata={
            "name": "targetDimensions",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    uses_parameter: List[UsesParameter] = field(
        default_factory=list,
        metadata={
            "name": "usesParameter",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class OperationParameterGroupType(OperationParameterGroupBaseType):
    """The definition of a group of parameters used by an operation method.

    This complexType is expected to be used or extended for all
    applicable operation methods, without defining operation-method-
    specialized element names.

    :ivar group_id: Set of alternative identifications of this operation
        parameter group. The first groupID, if any, is normally the
        primary identification code, and any others are aliases.
    :ivar remarks: Comments on or information about this operation
        parameter group, including source information.
    :ivar maximum_occurs:
    :ivar includes_parameter: Unordered list of associations to the set
        of operation parameters that are members of this group.
    """
    group_id: List[GroupId] = field(
        default_factory=list,
        metadata={
            "name": "groupID",
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
    maximum_occurs: Optional[int] = field(
        default=None,
        metadata={
            "name": "maximumOccurs",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    includes_parameter: List[IncludesParameter] = field(
        default_factory=list,
        metadata={
            "name": "includesParameter",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 2,
        }
    )


@dataclass
class ParameterValueType(AbstractGeneralParameterValueType):
    """A parameter value, ordered sequence of values, or reference to a file of
    parameter values.

    This concrete complexType can be used for operation methods without
    using an Application Schema that defines operation-method-
    specialized element names and contents, especially for methods with
    only one instance. This complexType can be used, extended, or
    restricted for well-known operation methods, especially for methods
    with many instances.
    """
    value: Optional[Value] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    dms_angle_value: Optional[DmsAngleValue] = field(
        default=None,
        metadata={
            "name": "dmsAngleValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    string_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "stringValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    integer_value: Optional[int] = field(
        default=None,
        metadata={
            "name": "integerValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    boolean_value: Optional[bool] = field(
        default=None,
        metadata={
            "name": "booleanValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    value_list: Optional[ValueList] = field(
        default=None,
        metadata={
            "name": "valueList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    integer_value_list: List[int] = field(
        default_factory=list,
        metadata={
            "name": "integerValueList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "tokens": True,
        }
    )
    value_file: Optional[str] = field(
        default=None,
        metadata={
            "name": "valueFile",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    value_of_parameter: Optional[ValueOfParameter] = field(
        default=None,
        metadata={
            "name": "valueOfParameter",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )


@dataclass
class OperationMethod(OperationMethodType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class OperationParameterGroup(OperationParameterGroupType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class ParameterValue(ParameterValueType):
    class Meta:
        name = "parameterValue"
        namespace = "http://www.opengis.net/gml"


@dataclass
class UsesValue(ParameterValueType):
    """
    Composition association to a parameter value used by this coordinate
    operation.
    """
    class Meta:
        name = "usesValue"
        namespace = "http://www.opengis.net/gml"


@dataclass
class OperationMethodRefType:
    """
    Association to a concrete general-purpose operation method, either
    referencing or containing the definition of that method.
    """
    operation_method: Optional[OperationMethod] = field(
        default=None,
        metadata={
            "name": "OperationMethod",
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
class OperationParameterGroupRefType:
    """
    Association to an operation parameter, either referencing or containing the
    definition of that parameter.
    """
    operation_parameter_group: Optional[OperationParameterGroup] = field(
        default=None,
        metadata={
            "name": "OperationParameterGroup",
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
class OperationMethodRef(OperationMethodRefType):
    class Meta:
        name = "operationMethodRef"
        namespace = "http://www.opengis.net/gml"


@dataclass
class UsesMethod(OperationMethodRefType):
    """
    Association to the operation method used by this coordinate operation.
    """
    class Meta:
        name = "usesMethod"
        namespace = "http://www.opengis.net/gml"


@dataclass
class ValuesOfGroup(OperationParameterGroupRefType):
    """
    Association to the operation parameter group for which this element
    provides parameter values.
    """
    class Meta:
        name = "valuesOfGroup"
        namespace = "http://www.opengis.net/gml"


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
class ParameterValueGroupType(AbstractGeneralParameterValueType):
    """A group of related parameter values.

    The same group can be repeated more than once in a Conversion,
    Transformation, or higher level parameterValueGroup, if those
    instances contain different values of one or more parameterValues
    which suitably distinquish among those groups. This concrete
    complexType can be used for operation methods without using an
    Application Schema that defines operation-method-specialized element
    names and contents, especially for methods with only one instance.
    This complexType can be used, extended, or restricted for well-known
    operation methods, especially for methods with many instances.

    :ivar includes_value: Unordered set of composition associations to
        the parameter values and groups of values included in this
        group.
    :ivar values_of_group:
    """
    includes_value: List[IncludesValue] = field(
        default_factory=list,
        metadata={
            "name": "includesValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 2,
        }
    )
    values_of_group: Optional[ValuesOfGroup] = field(
        default=None,
        metadata={
            "name": "valuesOfGroup",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )


@dataclass
class TransformationType(AbstractGeneralTransformationType):
    """A concrete operation on coordinates that usually includes a change of
    datum.

    The parameters of a coordinate transformation are empirically
    derived from data containing the coordinates of a series of points
    in both coordinate reference systems. This computational process is
    usually "over-determined", allowing derivation of error (or
    accuracy) estimates for the transformation. Also, the stochastic
    nature of the parameters may result in multiple (different) versions
    of the same coordinate transformation. This concrete complexType can
    be used for all operation methods, without using an Application
    Schema that defines operation-method-specialized element names and
    contents, especially for methods with only one Transformation
    instance.

    :ivar uses_method:
    :ivar uses_value: Unordered set of composition associations to the
        set of parameter values used by this transformation operation.
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
class Conversion(ConversionType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class Transformation(TransformationType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class ParameterValueGroup(ParameterValueGroupType):
    class Meta:
        name = "parameterValueGroup"
        namespace = "http://www.opengis.net/gml"


@dataclass
class ConversionRefType:
    """
    Association to a concrete general-purpose conversion, either referencing or
    containing the definition of that conversion.
    """
    conversion: Optional[Conversion] = field(
        default=None,
        metadata={
            "name": "Conversion",
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
class GeneralTransformationRefType:
    """
    Association to a general transformation, either referencing or containing
    the definition of that transformation.
    """
    transformation: Optional[Transformation] = field(
        default=None,
        metadata={
            "name": "Transformation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    general_transformation: Optional[GeneralTransformation] = field(
        default=None,
        metadata={
            "name": "_GeneralTransformation",
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
class OperationRefType:
    """
    Association to an abstract operation, either referencing or containing the
    definition of that operation.
    """
    transformation: Optional[Transformation] = field(
        default=None,
        metadata={
            "name": "Transformation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    general_transformation: Optional[GeneralTransformation] = field(
        default=None,
        metadata={
            "name": "_GeneralTransformation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    conversion: Optional[Conversion] = field(
        default=None,
        metadata={
            "name": "Conversion",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    general_conversion: Optional[GeneralConversion] = field(
        default=None,
        metadata={
            "name": "_GeneralConversion",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    operation: Optional[Operation] = field(
        default=None,
        metadata={
            "name": "_Operation",
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
class TransformationRefType:
    """
    Association to a transformation, either referencing or containing the
    definition of that transformation.
    """
    transformation: Optional[Transformation] = field(
        default=None,
        metadata={
            "name": "Transformation",
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
class ConversionRef(ConversionRefType):
    class Meta:
        name = "conversionRef"
        namespace = "http://www.opengis.net/gml"


@dataclass
class GeneralTransformationRef(GeneralTransformationRefType):
    class Meta:
        name = "generalTransformationRef"
        namespace = "http://www.opengis.net/gml"


@dataclass
class OperationRef(OperationRefType):
    class Meta:
        name = "operationRef"
        namespace = "http://www.opengis.net/gml"


@dataclass
class TransformationRef(TransformationRefType):
    class Meta:
        name = "transformationRef"
        namespace = "http://www.opengis.net/gml"


@dataclass
class UsesOperation(OperationRefType):
    """
    Association to the operation applied to the specified ordinates.
    """
    class Meta:
        name = "usesOperation"
        namespace = "http://www.opengis.net/gml"


@dataclass
class PassThroughOperationType(AbstractCoordinateOperationType):
    """
    A pass-through operation specifies that a subset of a coordinate tuple is
    subject to a specific coordinate operation.

    :ivar modified_coordinate: Ordered sequence of positive integers
        defining the positions in a coordinate tuple of the coordinates
        affected by this pass-through operation.
    :ivar uses_operation:
    """
    modified_coordinate: List[int] = field(
        default_factory=list,
        metadata={
            "name": "modifiedCoordinate",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        }
    )
    uses_operation: Optional[UsesOperation] = field(
        default=None,
        metadata={
            "name": "usesOperation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )


@dataclass
class PassThroughOperation(PassThroughOperationType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class PassThroughOperationRefType:
    """
    Association to a pass through operation, either referencing or containing
    the definition of that pass through operation.
    """
    pass_through_operation: Optional[PassThroughOperation] = field(
        default=None,
        metadata={
            "name": "PassThroughOperation",
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
class SingleOperationRefType:
    """
    Association to a single operation, either referencing or containing the
    definition of that single operation.
    """
    transformation: Optional[Transformation] = field(
        default=None,
        metadata={
            "name": "Transformation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    general_transformation: Optional[GeneralTransformation] = field(
        default=None,
        metadata={
            "name": "_GeneralTransformation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    conversion: Optional[Conversion] = field(
        default=None,
        metadata={
            "name": "Conversion",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    general_conversion: Optional[GeneralConversion] = field(
        default=None,
        metadata={
            "name": "_GeneralConversion",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    operation: Optional[Operation] = field(
        default=None,
        metadata={
            "name": "_Operation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    pass_through_operation: Optional[PassThroughOperation] = field(
        default=None,
        metadata={
            "name": "PassThroughOperation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    single_operation: Optional[SingleOperation] = field(
        default=None,
        metadata={
            "name": "_SingleOperation",
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
class PassThroughOperationRef(PassThroughOperationRefType):
    class Meta:
        name = "passThroughOperationRef"
        namespace = "http://www.opengis.net/gml"


@dataclass
class SingleOperationRef(SingleOperationRefType):
    class Meta:
        name = "singleOperationRef"
        namespace = "http://www.opengis.net/gml"


@dataclass
class UsesSingleOperation(SingleOperationRefType):
    """
    Association to a single operation.
    """
    class Meta:
        name = "usesSingleOperation"
        namespace = "http://www.opengis.net/gml"


@dataclass
class ConcatenatedOperationType(AbstractCoordinateOperationType):
    """An ordered sequence of two or more single coordinate operations.

    The sequence of operations is constrained by the requirement that
    the source coordinate reference system of step (n+1) must be the
    same as the target coordinate reference system of step (n). The
    source coordinate reference system of the first step and the target
    coordinate reference system of the last step are the source and
    target coordinate reference system associated with the concatenated
    operation. Instead of a forward operation, an inverse operation may
    be used for one or more of the operation steps mentioned above, if
    the inverse operation is uniquely defined by the forward operation.

    :ivar uses_single_operation: Ordered sequence of associations to the
        two or more single operations used by this concatenated
        operation.
    """
    uses_single_operation: List[UsesSingleOperation] = field(
        default_factory=list,
        metadata={
            "name": "usesSingleOperation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 2,
        }
    )


@dataclass
class ConcatenatedOperation(ConcatenatedOperationType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class ConcatenatedOperationRefType:
    """
    Association to a concatenated operation, either referencing or containing
    the definition of that concatenated operation.
    """
    concatenated_operation: Optional[ConcatenatedOperation] = field(
        default=None,
        metadata={
            "name": "ConcatenatedOperation",
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
class CoordinateOperationRefType:
    """
    Association to a coordinate operation, either referencing or containing the
    definition of that coordinate operation.
    """
    transformation: Optional[Transformation] = field(
        default=None,
        metadata={
            "name": "Transformation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    general_transformation: Optional[GeneralTransformation] = field(
        default=None,
        metadata={
            "name": "_GeneralTransformation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    conversion: Optional[Conversion] = field(
        default=None,
        metadata={
            "name": "Conversion",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    general_conversion: Optional[GeneralConversion] = field(
        default=None,
        metadata={
            "name": "_GeneralConversion",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    operation: Optional[Operation] = field(
        default=None,
        metadata={
            "name": "_Operation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    pass_through_operation: Optional[PassThroughOperation] = field(
        default=None,
        metadata={
            "name": "PassThroughOperation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    single_operation: Optional[SingleOperation] = field(
        default=None,
        metadata={
            "name": "_SingleOperation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    concatenated_operation: Optional[ConcatenatedOperation] = field(
        default=None,
        metadata={
            "name": "ConcatenatedOperation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    coordinate_operation: Optional[CoordinateOperation] = field(
        default=None,
        metadata={
            "name": "_CoordinateOperation",
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
class ConcatenatedOperationRef(ConcatenatedOperationRefType):
    class Meta:
        name = "concatenatedOperationRef"
        namespace = "http://www.opengis.net/gml"


@dataclass
class CoordinateOperationRef(CoordinateOperationRefType):
    class Meta:
        name = "coordinateOperationRef"
        namespace = "http://www.opengis.net/gml"
