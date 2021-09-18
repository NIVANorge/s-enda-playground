from dataclasses import dataclass, field
from typing import List, Optional
from generated.gml.pkg_3.pkg_1.pkg_1.base.basic_types import CodeType
from generated.gml.pkg_3.pkg_1.pkg_1.base.coordinate_operations import (
    CoordinateOperationName,
    GroupName,
    MethodName,
    ParameterName,
)
from generated.gml.pkg_3.pkg_1.pkg_1.base.datums import (
    DatumName,
    EllipsoidName,
    MeridianName,
)
from generated.gml.pkg_3.pkg_1.pkg_1.base.gml_base import (
    Description,
    MetaDataProperty,
    Name,
)
from generated.gml.pkg_3.pkg_1.pkg_1.base.reference_systems import (
    IdentifierType,
    Remarks,
    SrsName,
)
from generated.xlink import (
    ActuateType,
    ShowType,
    TypeType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AxisAbbrev(CodeType):
    """The abbreviation used for this coordinate system axis.

    This abbreviation can be used to identify the ordinates in a
    coordinate tuple. Examples are X and Y. The codeSpace attribute can
    reference a source of more information on a set of standardized
    abbreviations, or on this abbreviation.
    """
    class Meta:
        name = "axisAbbrev"
        namespace = "http://www.opengis.net/gml"


@dataclass
class AxisDirection(CodeType):
    """Direction of this coordinate system axis (or in the case of Cartesian
    projected coordinates, the direction of this coordinate system axis at the
    origin).

    Examples: north or south, east or west, up or down. Within any set of coordinate system axes, only one of each pair of terms can be used. For earth-fixed CRSs, this direction is often approximate and intended to provide a human interpretable meaning to the axis. When a geodetic datum is used, the precise directions of the axes may therefore vary slightly from this approximate direction. Note that an EngineeringCRS can include specific descriptions of the directions of its coordinate system axes. For example, the path of a linear CRS axis can be referenced in another document, such as referencing a GML feature that references or includes a curve geometry. The codeSpace attribute can reference a source of more information on a set of standardized directions, or on this direction.
    """
    class Meta:
        name = "axisDirection"
        namespace = "http://www.opengis.net/gml"


@dataclass
class AxisId(IdentifierType):
    """
    An identification of a coordinate system axis.
    """
    class Meta:
        name = "axisID"
        namespace = "http://www.opengis.net/gml"


@dataclass
class CsId(IdentifierType):
    """
    An identification of a coordinate system.
    """
    class Meta:
        name = "csID"
        namespace = "http://www.opengis.net/gml"


@dataclass
class CsName(CodeType):
    """
    The name by which this coordinate system is identified.
    """
    class Meta:
        name = "csName"
        namespace = "http://www.opengis.net/gml"


@dataclass
class AbstractCoordinateSystemBaseType:
    """
    Basic encoding for coordinate system objects, simplifying and restricting
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
    cs_name: Optional[CsName] = field(
        default=None,
        metadata={
            "name": "csName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
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
class CoordinateSystemAxisBaseType:
    """
    Basic encoding for coordinate system axis objects, simplifying and
    restricting the DefinitionType as needed.

    :ivar meta_data_property:
    :ivar description:
    :ivar group_name:
    :ivar parameter_name:
    :ivar method_name:
    :ivar coordinate_operation_name:
    :ivar ellipsoid_name:
    :ivar meridian_name:
    :ivar datum_name:
    :ivar cs_name:
    :ivar srs_name:
    :ivar name: The name by which this coordinate system axis is
        identified.
    :ivar id:
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
            "sequential": True,
        }
    )
    parameter_name: List[ParameterName] = field(
        default_factory=list,
        metadata={
            "name": "parameterName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        }
    )
    method_name: List[MethodName] = field(
        default_factory=list,
        metadata={
            "name": "methodName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        }
    )
    coordinate_operation_name: List[CoordinateOperationName] = field(
        default_factory=list,
        metadata={
            "name": "coordinateOperationName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        }
    )
    ellipsoid_name: List[EllipsoidName] = field(
        default_factory=list,
        metadata={
            "name": "ellipsoidName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        }
    )
    meridian_name: List[MeridianName] = field(
        default_factory=list,
        metadata={
            "name": "meridianName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        }
    )
    datum_name: List[DatumName] = field(
        default_factory=list,
        metadata={
            "name": "datumName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        }
    )
    cs_name: List[CsName] = field(
        default_factory=list,
        metadata={
            "name": "csName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        }
    )
    srs_name: List[SrsName] = field(
        default_factory=list,
        metadata={
            "name": "srsName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        }
    )
    name: Optional[Name] = field(
        default=None,
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
class CoordinateSystemAxisType(CoordinateSystemAxisBaseType):
    """
    Definition of a coordinate system axis.

    :ivar axis_id: Set of alternative identifications of this coordinate
        system axis. The first axisID, if any, is normally the primary
        identification code, and any others are aliases.
    :ivar remarks: Comments on or information about this coordinate
        system axis, including data source information.
    :ivar axis_abbrev:
    :ivar axis_direction:
    :ivar uom:
    """
    axis_id: List[AxisId] = field(
        default_factory=list,
        metadata={
            "name": "axisID",
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
    axis_abbrev: Optional[AxisAbbrev] = field(
        default=None,
        metadata={
            "name": "axisAbbrev",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    axis_direction: Optional[AxisDirection] = field(
        default=None,
        metadata={
            "name": "axisDirection",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    uom: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )


@dataclass
class CoordinateSystemAxis(CoordinateSystemAxisType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class CoordinateSystemAxisRefType:
    """
    Association to a coordinate system axis, either referencing or containing
    the definition of that axis.
    """
    coordinate_system_axis: Optional[CoordinateSystemAxis] = field(
        default=None,
        metadata={
            "name": "CoordinateSystemAxis",
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
class CoordinateSystemAxisRef(CoordinateSystemAxisRefType):
    class Meta:
        name = "coordinateSystemAxisRef"
        namespace = "http://www.opengis.net/gml"


@dataclass
class UsesAxis(CoordinateSystemAxisRefType):
    """
    Association to a coordinate system axis.
    """
    class Meta:
        name = "usesAxis"
        namespace = "http://www.opengis.net/gml"


@dataclass
class AbstractCoordinateSystemType(AbstractCoordinateSystemBaseType):
    """A coordinate system (CS) is the set of coordinate system axes that spans
    a given coordinate space.

    A CS is derived from a set of (mathematical) rules for specifying
    how coordinates in a given space are to be assigned to points. The
    coordinate values in a coordinate tuple shall be recorded in the
    order in which the coordinate system axes associations are recorded,
    whenever those coordinates use a coordinate reference system that
    uses this coordinate system. This abstract complexType shall not be
    used, extended, or restricted, in an Application Schema, to define a
    concrete subtype with a meaning equivalent to a concrete subtype
    specified in this document.

    :ivar cs_id: Set of alternative identifications of this coordinate
        system. The first csID, if any, is normally the primary
        identification code, and any others are aliases.
    :ivar remarks: Comments on or information about this coordinate
        system, including data source information.
    :ivar uses_axis: Ordered sequence of associations to the coordinate
        system axes included in this coordinate system.
    """
    cs_id: List[CsId] = field(
        default_factory=list,
        metadata={
            "name": "csID",
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
    uses_axis: List[UsesAxis] = field(
        default_factory=list,
        metadata={
            "name": "usesAxis",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        }
    )


@dataclass
class CartesianCstype(AbstractCoordinateSystemType):
    """A 1-, 2-, or 3-dimensional coordinate system.

    Gives the position of points relative to orthogonal straight axes in
    the 2- and 3-dimensional cases. In the 1-dimensional case, it
    contains a single straight coordinate axis. In the multi-dimensional
    case, all axes shall have the same length unit of measure. A
    CartesianCS shall have one, two, or three usesAxis associations.
    """
    class Meta:
        name = "CartesianCSType"


@dataclass
class CylindricalCstype(AbstractCoordinateSystemType):
    """A three-dimensional coordinate system consisting of a polar coordinate
    system extended by a straight coordinate axis perpendicular to the plane
    spanned by the polar coordinate system.

    A CylindricalCS shall have three usesAxis associations.
    """
    class Meta:
        name = "CylindricalCSType"


@dataclass
class EllipsoidalCstype(AbstractCoordinateSystemType):
    """A two- or three-dimensional coordinate system in which position is
    specified by geodetic latitude, geodetic longitude, and (in the three-
    dimensional case) ellipsoidal height.

    An EllipsoidalCS shall have two or three usesAxis associations.
    """
    class Meta:
        name = "EllipsoidalCSType"


@dataclass
class LinearCstype(AbstractCoordinateSystemType):
    """A one-dimensional coordinate system that consists of the points that lie
    on the single axis described.

    The associated ordinate is the distance from the specified origin to
    the point along the axis. Example: usage of the line feature
    representing a road to describe points on or along that road. A
    LinearCS shall have one usesAxis association.
    """
    class Meta:
        name = "LinearCSType"


@dataclass
class ObliqueCartesianCstype(AbstractCoordinateSystemType):
    """A two- or three-dimensional coordinate system with straight axes that
    are not necessarily orthogonal.

    An ObliqueCartesianCS shall have two or three usesAxis associations.
    """
    class Meta:
        name = "ObliqueCartesianCSType"


@dataclass
class PolarCstype(AbstractCoordinateSystemType):
    """A two-dimensional coordinate system in which position is specified by
    the distance from the origin and the angle between the line from the origin
    to a point and a reference direction.

    A PolarCS shall have two usesAxis associations.
    """
    class Meta:
        name = "PolarCSType"


@dataclass
class SphericalCstype(AbstractCoordinateSystemType):
    """A three-dimensional coordinate system with one distance measured from
    the origin and two angular coordinates.

    Not to be confused with an ellipsoidal coordinate system based on an
    ellipsoid "degenerated" into a sphere. A SphericalCS shall have
    three usesAxis associations.
    """
    class Meta:
        name = "SphericalCSType"


@dataclass
class TemporalCstype(AbstractCoordinateSystemType):
    """A one-dimensional coordinate system containing a single time axis, used
    to describe the temporal position of a point in the specified time units
    from a specified time origin.

    A TemporalCS shall have one usesAxis association.
    """
    class Meta:
        name = "TemporalCSType"


@dataclass
class UserDefinedCstype(AbstractCoordinateSystemType):
    """A two- or three-dimensional coordinate system that consists of any
    combination of coordinate axes not covered by any other coordinate system
    type.

    An example is a multilinear coordinate system which contains one
    coordinate axis that may have any 1-D shape which has no
    intersections with itself. This non-straight axis is supplemented by
    one or two straight axes to complete a 2 or 3 dimensional coordinate
    system. The non-straight axis is typically incrementally straight or
    curved. A UserDefinedCS shall have two or three usesAxis
    associations.
    """
    class Meta:
        name = "UserDefinedCSType"


@dataclass
class VerticalCstype(AbstractCoordinateSystemType):
    """A one-dimensional coordinate system used to record the heights (or
    depths) of points.

    Such a coordinate system is usually dependent on the Earth's gravity
    field, perhaps loosely as when atmospheric pressure is the basis for
    the vertical coordinate system axis. A VerticalCS shall have one
    usesAxis association.
    """
    class Meta:
        name = "VerticalCSType"


@dataclass
class CoordinateSystem(AbstractCoordinateSystemType):
    class Meta:
        name = "_CoordinateSystem"
        namespace = "http://www.opengis.net/gml"


@dataclass
class CartesianCs(CartesianCstype):
    class Meta:
        name = "CartesianCS"
        namespace = "http://www.opengis.net/gml"


@dataclass
class CylindricalCs(CylindricalCstype):
    class Meta:
        name = "CylindricalCS"
        namespace = "http://www.opengis.net/gml"


@dataclass
class EllipsoidalCs(EllipsoidalCstype):
    class Meta:
        name = "EllipsoidalCS"
        namespace = "http://www.opengis.net/gml"


@dataclass
class LinearCs(LinearCstype):
    class Meta:
        name = "LinearCS"
        namespace = "http://www.opengis.net/gml"


@dataclass
class ObliqueCartesianCs(ObliqueCartesianCstype):
    class Meta:
        name = "ObliqueCartesianCS"
        namespace = "http://www.opengis.net/gml"


@dataclass
class PolarCs(PolarCstype):
    class Meta:
        name = "PolarCS"
        namespace = "http://www.opengis.net/gml"


@dataclass
class SphericalCs(SphericalCstype):
    class Meta:
        name = "SphericalCS"
        namespace = "http://www.opengis.net/gml"


@dataclass
class TemporalCs(TemporalCstype):
    class Meta:
        name = "TemporalCS"
        namespace = "http://www.opengis.net/gml"


@dataclass
class UserDefinedCs(UserDefinedCstype):
    class Meta:
        name = "UserDefinedCS"
        namespace = "http://www.opengis.net/gml"


@dataclass
class VerticalCs(VerticalCstype):
    class Meta:
        name = "VerticalCS"
        namespace = "http://www.opengis.net/gml"


@dataclass
class CartesianCsrefType:
    """
    Association to a Cartesian coordinate system, either referencing or
    containing the definition of that coordinate system.
    """
    class Meta:
        name = "CartesianCSRefType"

    cartesian_cs: Optional[CartesianCs] = field(
        default=None,
        metadata={
            "name": "CartesianCS",
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
class CoordinateSystemRefType:
    """
    Association to a coordinate system, either referencing or containing the
    definition of that coordinate system.
    """
    oblique_cartesian_cs: Optional[ObliqueCartesianCs] = field(
        default=None,
        metadata={
            "name": "ObliqueCartesianCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    cylindrical_cs: Optional[CylindricalCs] = field(
        default=None,
        metadata={
            "name": "CylindricalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    polar_cs: Optional[PolarCs] = field(
        default=None,
        metadata={
            "name": "PolarCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    spherical_cs: Optional[SphericalCs] = field(
        default=None,
        metadata={
            "name": "SphericalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    user_defined_cs: Optional[UserDefinedCs] = field(
        default=None,
        metadata={
            "name": "UserDefinedCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    linear_cs: Optional[LinearCs] = field(
        default=None,
        metadata={
            "name": "LinearCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    temporal_cs: Optional[TemporalCs] = field(
        default=None,
        metadata={
            "name": "TemporalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    vertical_cs: Optional[VerticalCs] = field(
        default=None,
        metadata={
            "name": "VerticalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    cartesian_cs: Optional[CartesianCs] = field(
        default=None,
        metadata={
            "name": "CartesianCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    ellipsoidal_cs: Optional[EllipsoidalCs] = field(
        default=None,
        metadata={
            "name": "EllipsoidalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    coordinate_system: Optional[CoordinateSystem] = field(
        default=None,
        metadata={
            "name": "_CoordinateSystem",
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
class CylindricalCsrefType:
    """
    Association to a cylindrical coordinate system, either referencing or
    containing the definition of that coordinate system.
    """
    class Meta:
        name = "CylindricalCSRefType"

    cylindrical_cs: Optional[CylindricalCs] = field(
        default=None,
        metadata={
            "name": "CylindricalCS",
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
class EllipsoidalCsrefType:
    """
    Association to an ellipsoidal coordinate system, either referencing or
    containing the definition of that coordinate system.
    """
    class Meta:
        name = "EllipsoidalCSRefType"

    ellipsoidal_cs: Optional[EllipsoidalCs] = field(
        default=None,
        metadata={
            "name": "EllipsoidalCS",
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
class LinearCsrefType:
    """
    Association to a linear coordinate system, either referencing or containing
    the definition of that coordinate system.
    """
    class Meta:
        name = "LinearCSRefType"

    linear_cs: Optional[LinearCs] = field(
        default=None,
        metadata={
            "name": "LinearCS",
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
class ObliqueCartesianCsrefType:
    """
    Association to an oblique-Cartesian coordinate system, either referencing
    or containing the definition of that coordinate system.
    """
    class Meta:
        name = "ObliqueCartesianCSRefType"

    oblique_cartesian_cs: Optional[ObliqueCartesianCs] = field(
        default=None,
        metadata={
            "name": "ObliqueCartesianCS",
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
class PolarCsrefType:
    """
    Association to a polar coordinate system, either referencing or containing
    the definition of that coordinate system.
    """
    class Meta:
        name = "PolarCSRefType"

    polar_cs: Optional[PolarCs] = field(
        default=None,
        metadata={
            "name": "PolarCS",
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
class SphericalCsrefType:
    """
    Association to a spherical coordinate system, either referencing or
    containing the definition of that coordinate system.
    """
    class Meta:
        name = "SphericalCSRefType"

    spherical_cs: Optional[SphericalCs] = field(
        default=None,
        metadata={
            "name": "SphericalCS",
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
class TemporalCsrefType:
    """
    Association to a temporal coordinate system, either referencing or
    containing the definition of that coordinate system.
    """
    class Meta:
        name = "TemporalCSRefType"

    temporal_cs: Optional[TemporalCs] = field(
        default=None,
        metadata={
            "name": "TemporalCS",
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
class UserDefinedCsrefType:
    """
    Association to a user-defined coordinate system, either referencing or
    containing the definition of that coordinate system.
    """
    class Meta:
        name = "UserDefinedCSRefType"

    user_defined_cs: Optional[UserDefinedCs] = field(
        default=None,
        metadata={
            "name": "UserDefinedCS",
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
class VerticalCsrefType:
    """
    Association to a vertical coordinate system, either referencing or
    containing the definition of that coordinate system.
    """
    class Meta:
        name = "VerticalCSRefType"

    vertical_cs: Optional[VerticalCs] = field(
        default=None,
        metadata={
            "name": "VerticalCS",
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
class CartesianCsref(CartesianCsrefType):
    class Meta:
        name = "cartesianCSRef"
        namespace = "http://www.opengis.net/gml"


@dataclass
class CoordinateSystemRef(CoordinateSystemRefType):
    class Meta:
        name = "coordinateSystemRef"
        namespace = "http://www.opengis.net/gml"


@dataclass
class CylindricalCsref(CylindricalCsrefType):
    class Meta:
        name = "cylindricalCSRef"
        namespace = "http://www.opengis.net/gml"


@dataclass
class EllipsoidalCsref(EllipsoidalCsrefType):
    class Meta:
        name = "ellipsoidalCSRef"
        namespace = "http://www.opengis.net/gml"


@dataclass
class LinearCsref(LinearCsrefType):
    class Meta:
        name = "linearCSRef"
        namespace = "http://www.opengis.net/gml"


@dataclass
class ObliqueCartesianCsref(ObliqueCartesianCsrefType):
    class Meta:
        name = "obliqueCartesianCSRef"
        namespace = "http://www.opengis.net/gml"


@dataclass
class PolarCsref(PolarCsrefType):
    class Meta:
        name = "polarCSRef"
        namespace = "http://www.opengis.net/gml"


@dataclass
class SphericalCsref(SphericalCsrefType):
    class Meta:
        name = "sphericalCSRef"
        namespace = "http://www.opengis.net/gml"


@dataclass
class TemporalCsref(TemporalCsrefType):
    class Meta:
        name = "temporalCSRef"
        namespace = "http://www.opengis.net/gml"


@dataclass
class UserDefinedCsref(UserDefinedCsrefType):
    class Meta:
        name = "userDefinedCSRef"
        namespace = "http://www.opengis.net/gml"


@dataclass
class VerticalCsref(VerticalCsrefType):
    class Meta:
        name = "verticalCSRef"
        namespace = "http://www.opengis.net/gml"
