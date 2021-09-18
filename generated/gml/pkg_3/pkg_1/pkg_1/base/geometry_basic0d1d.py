from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional
from generated.gml.pkg_3.pkg_1.pkg_1.base.basic_types import CoordinatesType
from generated.gml.pkg_3.pkg_1.pkg_1.base.coordinate_operations import (
    CoordinateOperationName,
    GroupName,
    MethodName,
    ParameterName,
)
from generated.gml.pkg_3.pkg_1.pkg_1.base.coordinate_systems import CsName
from generated.gml.pkg_3.pkg_1.pkg_1.base.datums import (
    DatumName,
    EllipsoidName,
    MeridianName,
)
from generated.gml.pkg_3.pkg_1.pkg_1.base.geometry_aggregates import (
    MultiCurve,
    MultiLineString,
    MultiPoint,
    MultiPolygon,
    MultiSolid,
    MultiSurface,
    GeometricAggregate,
)
from generated.gml.pkg_3.pkg_1.pkg_1.base.geometry_basic2d import (
    LinearRing,
    Polygon,
    Ring2,
    Surface2,
)
from generated.gml.pkg_3.pkg_1.pkg_1.base.geometry_complexes import (
    CompositeCurve,
    CompositeSolid,
    CompositeSurface,
    GeometricComplex,
)
from generated.gml.pkg_3.pkg_1.pkg_1.base.geometry_primitives import (
    Curve1,
    OrientableCurve,
    OrientableSurface,
    PolyhedralSurface,
    Ring1,
    Solid1,
    Surface1,
    Tin,
    TriangulatedSurface,
    Solid2,
)
from generated.gml.pkg_3.pkg_1.pkg_1.base.gml_base import (
    Description,
    MetaDataProperty,
    Name,
)
from generated.gml.pkg_3.pkg_1.pkg_1.base.grids import (
    Grid,
    RectifiedGrid,
    ImplicitGeometry,
)
from generated.xlink import (
    ActuateType,
    ShowType,
    TypeType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CoordType:
    """Represents a coordinate tuple in one, two, or three dimensions.

    Deprecated with GML 3.0 and replaced by DirectPositionType.
    """
    x: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "X",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    y: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Y",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    z: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Z",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class DirectPositionListType:
    """
    DirectPositionList instances hold the coordinates for a sequence of direct
    positions within the same coordinate reference system (CRS).

    :ivar value:
    :ivar srs_name: In general this reference points to a CRS instance
        of gml:CoordinateReferenceSystemType (see
        coordinateReferenceSystems.xsd). For well known references it is
        not required that the CRS description exists at the location the
        URI points to. If no srsName attribute is given, the CRS must be
        specified as part of the larger context this geometry element is
        part of, e.g. a geometric element like point, curve, etc. It is
        expected that this attribute will be specified at the direct
        position level only in rare cases.
    :ivar srs_dimension: The "srsDimension" is the length of coordinate
        sequence (the number of entries in the list). This dimension is
        specified by the coordinate reference system. When the srsName
        attribute is omitted, this attribute shall be omitted.
    :ivar axis_labels: Ordered list of labels for all the axes of this
        CRS. The gml:axisAbbrev value should be used for these axis
        labels, after spaces and forbiddden characters are removed. When
        the srsName attribute is included, this attribute is optional.
        When the srsName attribute is omitted, this attribute shall also
        be omitted.
    :ivar uom_labels: Ordered list of unit of measure (uom) labels for
        all the axes of this CRS. The value of the string in the
        gml:catalogSymbol should be used for this uom labels, after
        spaces and forbiddden characters are removed. When the
        axisLabels attribute is included, this attribute shall also be
        included. When the axisLabels attribute is omitted, this
        attribute shall also be omitted.
    :ivar count: "count" allows to specify the number of direct
        positions in the list. If the attribute count is present then
        the attribute srsDimension shall be present, too.
    """
    value: List[float] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        }
    )
    srs_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "srsName",
            "type": "Attribute",
        }
    )
    srs_dimension: Optional[int] = field(
        default=None,
        metadata={
            "name": "srsDimension",
            "type": "Attribute",
        }
    )
    axis_labels: List[str] = field(
        default_factory=list,
        metadata={
            "name": "axisLabels",
            "type": "Attribute",
            "tokens": True,
        }
    )
    uom_labels: List[str] = field(
        default_factory=list,
        metadata={
            "name": "uomLabels",
            "type": "Attribute",
            "tokens": True,
        }
    )
    count: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class DirectPositionType:
    """DirectPosition instances hold the coordinates for a position within some
    coordinate reference system (CRS).

    Since DirectPositions, as data types, will often be included in
    larger objects (such as geometry elements) that have references to
    CRS, the "srsName" attribute will in general be missing, if this
    particular DirectPosition is included in a larger element with such
    a reference to a CRS. In this case, the CRS is implicitly assumed to
    take on the value of the containing object's CRS.

    :ivar value:
    :ivar srs_name: In general this reference points to a CRS instance
        of gml:CoordinateReferenceSystemType (see
        coordinateReferenceSystems.xsd). For well known references it is
        not required that the CRS description exists at the location the
        URI points to. If no srsName attribute is given, the CRS must be
        specified as part of the larger context this geometry element is
        part of, e.g. a geometric element like point, curve, etc. It is
        expected that this attribute will be specified at the direct
        position level only in rare cases.
    :ivar srs_dimension: The "srsDimension" is the length of coordinate
        sequence (the number of entries in the list). This dimension is
        specified by the coordinate reference system. When the srsName
        attribute is omitted, this attribute shall be omitted.
    :ivar axis_labels: Ordered list of labels for all the axes of this
        CRS. The gml:axisAbbrev value should be used for these axis
        labels, after spaces and forbiddden characters are removed. When
        the srsName attribute is included, this attribute is optional.
        When the srsName attribute is omitted, this attribute shall also
        be omitted.
    :ivar uom_labels: Ordered list of unit of measure (uom) labels for
        all the axes of this CRS. The value of the string in the
        gml:catalogSymbol should be used for this uom labels, after
        spaces and forbiddden characters are removed. When the
        axisLabels attribute is included, this attribute shall also be
        included. When the axisLabels attribute is omitted, this
        attribute shall also be omitted.
    """
    value: List[float] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        }
    )
    srs_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "srsName",
            "type": "Attribute",
        }
    )
    srs_dimension: Optional[int] = field(
        default=None,
        metadata={
            "name": "srsDimension",
            "type": "Attribute",
        }
    )
    axis_labels: List[str] = field(
        default_factory=list,
        metadata={
            "name": "axisLabels",
            "type": "Attribute",
            "tokens": True,
        }
    )
    uom_labels: List[str] = field(
        default_factory=list,
        metadata={
            "name": "uomLabels",
            "type": "Attribute",
            "tokens": True,
        }
    )


@dataclass
class VectorType:
    """Vector instances hold the compoents for a (usually spatial) vector
    within some coordinate reference system (CRS).

    Since Vectors will often be included in larger objects that have
    references to CRS, the "srsName" attribute may be missing. In this
    case, the CRS is implicitly assumed to take on the value of the
    containing object's CRS. Note that this content model is the same as
    DirectPositionType, but is defined separately to reflect the
    distinct semantics, and to avoid validation problems. SJDC
    2004-12-02

    :ivar value:
    :ivar srs_name: In general this reference points to a CRS instance
        of gml:CoordinateReferenceSystemType (see
        coordinateReferenceSystems.xsd). For well known references it is
        not required that the CRS description exists at the location the
        URI points to. If no srsName attribute is given, the CRS must be
        specified as part of the larger context this geometry element is
        part of, e.g. a geometric element like point, curve, etc. It is
        expected that this attribute will be specified at the direct
        position level only in rare cases.
    :ivar srs_dimension: The "srsDimension" is the length of coordinate
        sequence (the number of entries in the list). This dimension is
        specified by the coordinate reference system. When the srsName
        attribute is omitted, this attribute shall be omitted.
    :ivar axis_labels: Ordered list of labels for all the axes of this
        CRS. The gml:axisAbbrev value should be used for these axis
        labels, after spaces and forbiddden characters are removed. When
        the srsName attribute is included, this attribute is optional.
        When the srsName attribute is omitted, this attribute shall also
        be omitted.
    :ivar uom_labels: Ordered list of unit of measure (uom) labels for
        all the axes of this CRS. The value of the string in the
        gml:catalogSymbol should be used for this uom labels, after
        spaces and forbiddden characters are removed. When the
        axisLabels attribute is included, this attribute shall also be
        included. When the axisLabels attribute is omitted, this
        attribute shall also be omitted.
    """
    value: List[float] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        }
    )
    srs_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "srsName",
            "type": "Attribute",
        }
    )
    srs_dimension: Optional[int] = field(
        default=None,
        metadata={
            "name": "srsDimension",
            "type": "Attribute",
        }
    )
    axis_labels: List[str] = field(
        default_factory=list,
        metadata={
            "name": "axisLabels",
            "type": "Attribute",
            "tokens": True,
        }
    )
    uom_labels: List[str] = field(
        default_factory=list,
        metadata={
            "name": "uomLabels",
            "type": "Attribute",
            "tokens": True,
        }
    )


@dataclass
class AbstractGeometryType:
    """All geometry elements are derived directly or indirectly from this
    abstract supertype. A geometry element may have an identifying attribute
    ("gml:id"), a name (attribute "name") and a description (attribute
    "description"). It may be associated.

    with a spatial reference system (attribute "srsName"). The following rules shall be adhered: - Every geometry type shall derive
    from this abstract type. - Every geometry element (i.e. an element of a geometry type) shall be directly or indirectly in the
    substitution group of _Geometry.

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
    :ivar gid: This attribute is included for backward compatibility
        with GML 2 and is deprecated with GML 3. This identifer is
        superceded by "gml:id" inherited from AbstractGMLType. The
        attribute "gid" should not be used anymore and may be deleted in
        future versions of GML without further notice.
    :ivar name: Multiple names may be provided.  These will often be
        distinguished by being assigned by different authorities, as
        indicated by the value of the codeSpace attribute.  In an
        instance document there will usually only be one name per
        authority.
    :ivar id:
    :ivar srs_name_attribute: In general this reference points to a CRS
        instance of gml:CoordinateReferenceSystemType (see
        coordinateReferenceSystems.xsd). For well known references it is
        not required that the CRS description exists at the location the
        URI points to. If no srsName attribute is given, the CRS must be
        specified as part of the larger context this geometry element is
        part of, e.g. a geometric element like point, curve, etc. It is
        expected that this attribute will be specified at the direct
        position level only in rare cases.
    :ivar srs_dimension: The "srsDimension" is the length of coordinate
        sequence (the number of entries in the list). This dimension is
        specified by the coordinate reference system. When the srsName
        attribute is omitted, this attribute shall be omitted.
    :ivar axis_labels: Ordered list of labels for all the axes of this
        CRS. The gml:axisAbbrev value should be used for these axis
        labels, after spaces and forbiddden characters are removed. When
        the srsName attribute is included, this attribute is optional.
        When the srsName attribute is omitted, this attribute shall also
        be omitted.
    :ivar uom_labels: Ordered list of unit of measure (uom) labels for
        all the axes of this CRS. The value of the string in the
        gml:catalogSymbol should be used for this uom labels, after
        spaces and forbiddden characters are removed. When the
        axisLabels attribute is included, this attribute shall also be
        included. When the axisLabels attribute is omitted, this
        attribute shall also be omitted.
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
    gid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
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
        }
    )
    srs_name_attribute: Optional[str] = field(
        default=None,
        metadata={
            "name": "srsName",
            "type": "Attribute",
        }
    )
    srs_dimension: Optional[int] = field(
        default=None,
        metadata={
            "name": "srsDimension",
            "type": "Attribute",
        }
    )
    axis_labels: List[str] = field(
        default_factory=list,
        metadata={
            "name": "axisLabels",
            "type": "Attribute",
            "tokens": True,
        }
    )
    uom_labels: List[str] = field(
        default_factory=list,
        metadata={
            "name": "uomLabels",
            "type": "Attribute",
            "tokens": True,
        }
    )


@dataclass
class Coord(CoordType):
    """Deprecated with GML 3.0 and included for backwards compatibility with
    GML 2.

    Use the "pos" element instead.
    """
    class Meta:
        name = "coord"
        namespace = "http://www.opengis.net/gml"


@dataclass
class Coordinates(CoordinatesType):
    """
    Deprecated with GML version 3.1.0.
    """
    class Meta:
        name = "coordinates"
        namespace = "http://www.opengis.net/gml"


@dataclass
class Pos(DirectPositionType):
    class Meta:
        name = "pos"
        namespace = "http://www.opengis.net/gml"


@dataclass
class PosList(DirectPositionListType):
    class Meta:
        name = "posList"
        namespace = "http://www.opengis.net/gml"


@dataclass
class Vector(VectorType):
    class Meta:
        name = "vector"
        namespace = "http://www.opengis.net/gml"


@dataclass
class AbstractGeometricPrimitiveType(AbstractGeometryType):
    """This is the abstract root type of the geometric primitives.

    A geometric primitive is a geometric object that is not decomposed
    further into other primitives in the system. All primitives are
    oriented in the direction implied by the sequence of their
    coordinate tuples.
    """


@dataclass
class EnvelopeType:
    """Envelope defines an extent using a pair of positions defining opposite
    corners in arbitrary dimensions.

    The first direct position is the "lower corner" (a coordinate
    position consisting of all the minimal ordinates for each dimension
    for all points within the envelope), the second one the "upper
    corner" (a coordinate position consisting of all the maximal
    ordinates for each dimension for all points within the envelope).

    :ivar lower_corner:
    :ivar upper_corner:
    :ivar coord: deprecated with GML version 3.0
    :ivar pos: Deprecated with GML version 3.1. Use the explicit
        properties "lowerCorner" and "upperCorner" instead.
    :ivar coordinates: Deprecated with GML version 3.1.0. Use the
        explicit properties "lowerCorner" and "upperCorner" instead.
    :ivar srs_name: In general this reference points to a CRS instance
        of gml:CoordinateReferenceSystemType (see
        coordinateReferenceSystems.xsd). For well known references it is
        not required that the CRS description exists at the location the
        URI points to. If no srsName attribute is given, the CRS must be
        specified as part of the larger context this geometry element is
        part of, e.g. a geometric element like point, curve, etc. It is
        expected that this attribute will be specified at the direct
        position level only in rare cases.
    :ivar srs_dimension: The "srsDimension" is the length of coordinate
        sequence (the number of entries in the list). This dimension is
        specified by the coordinate reference system. When the srsName
        attribute is omitted, this attribute shall be omitted.
    :ivar axis_labels: Ordered list of labels for all the axes of this
        CRS. The gml:axisAbbrev value should be used for these axis
        labels, after spaces and forbiddden characters are removed. When
        the srsName attribute is included, this attribute is optional.
        When the srsName attribute is omitted, this attribute shall also
        be omitted.
    :ivar uom_labels: Ordered list of unit of measure (uom) labels for
        all the axes of this CRS. The value of the string in the
        gml:catalogSymbol should be used for this uom labels, after
        spaces and forbiddden characters are removed. When the
        axisLabels attribute is included, this attribute shall also be
        included. When the axisLabels attribute is omitted, this
        attribute shall also be omitted.
    """
    lower_corner: Optional[DirectPositionType] = field(
        default=None,
        metadata={
            "name": "lowerCorner",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    upper_corner: Optional[DirectPositionType] = field(
        default=None,
        metadata={
            "name": "upperCorner",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    coord: List[Coord] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "max_occurs": 2,
        }
    )
    pos: List[Pos] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "max_occurs": 2,
        }
    )
    coordinates: Optional[Coordinates] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    srs_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "srsName",
            "type": "Attribute",
        }
    )
    srs_dimension: Optional[int] = field(
        default=None,
        metadata={
            "name": "srsDimension",
            "type": "Attribute",
        }
    )
    axis_labels: List[str] = field(
        default_factory=list,
        metadata={
            "name": "axisLabels",
            "type": "Attribute",
            "tokens": True,
        }
    )
    uom_labels: List[str] = field(
        default_factory=list,
        metadata={
            "name": "uomLabels",
            "type": "Attribute",
            "tokens": True,
        }
    )


@dataclass
class Geometry(AbstractGeometryType):
    """The "_Geometry" element is the abstract head of the substituition group
    for all geometry elements of GML 3.

    This includes pre-defined and user-defined geometry elements. Any
    geometry element must be a direct or indirect extension/restriction
    of AbstractGeometryType and must be directly or indirectly in the
    substitution group of "_Geometry".
    """
    class Meta:
        name = "_Geometry"
        namespace = "http://www.opengis.net/gml"


@dataclass
class AbstractCurveType(AbstractGeometricPrimitiveType):
    """An abstraction of a curve to support the different levels of complexity.

    The curve can always be viewed as a geometric primitive, i.e. is
    continuous.
    """


@dataclass
class Envelope(EnvelopeType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class PointType(AbstractGeometricPrimitiveType):
    """
    A Point is defined by a single coordinate tuple.

    :ivar pos:
    :ivar coordinates: Deprecated with GML version 3.1.0 for coordinates
        with ordinate values that are numbers. Use "pos" instead. The
        "coordinates" element shall only be used for coordinates with
        ordinates that require a string representation, e.g. DMS
        representations.
    :ivar coord: Deprecated with GML version 3.0. Use "pos" instead. The
        "coord" element is included for backwards compatibility with GML
        2.
    """
    pos: Optional[Pos] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    coordinates: Optional[Coordinates] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    coord: Optional[Coord] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class GeometricPrimitive(AbstractGeometricPrimitiveType):
    """
    The "_GeometricPrimitive" element is the abstract head of the substituition
    group for all (pre- and user-defined) geometric primitives.
    """
    class Meta:
        name = "_GeometricPrimitive"
        namespace = "http://www.opengis.net/gml"


@dataclass
class Point(PointType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class Curve2(AbstractCurveType):
    """
    The "_Curve" element is the abstract head of the substituition group for
    all (continuous) curve elements.
    """
    class Meta:
        name = "_Curve"
        namespace = "http://www.opengis.net/gml"


@dataclass
class PointArrayPropertyType:
    """A container for an array of points.

    The elements are always contained in the array property, referencing
    geometry elements or arrays of geometry elements is not supported.
    """
    point: List[Point] = field(
        default_factory=list,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class PointPropertyType:
    """A property that has a point as its value domain can either be an
    appropriate geometry element encapsulated in an element of this type or an
    XLink reference to a remote geometry element (where remote includes
    geometry elements located elsewhere in the same document).

    Either the reference or the contained element must be given, but
    neither both nor none.
    """
    point: Optional[Point] = field(
        default=None,
        metadata={
            "name": "Point",
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
class PointArrayProperty(PointArrayPropertyType):
    class Meta:
        name = "pointArrayProperty"
        namespace = "http://www.opengis.net/gml"


@dataclass
class PointProperty(PointPropertyType):
    """This property element either references a point via the XLink-attributes
    or contains the point element.

    pointProperty is the predefined property which can be used by GML
    Application Schemas whenever a GML Feature has a property with a
    value that is substitutable for Point.
    """
    class Meta:
        name = "pointProperty"
        namespace = "http://www.opengis.net/gml"


@dataclass
class PointRep(PointPropertyType):
    """Deprecated with GML version 3.1.0.

    Use "pointProperty" instead. Included for backwards compatibility
    with GML 3.0.0.
    """
    class Meta:
        name = "pointRep"
        namespace = "http://www.opengis.net/gml"


@dataclass
class LineStringType(AbstractCurveType):
    """A LineString is a special curve that consists of a single segment with
    linear interpolation.

    It is defined by two or more coordinate tuples, with linear
    interpolation between them. It is backwards compatible with the
    LineString of GML 2, GM_LineString of ISO 19107 is implemented by
    LineStringSegment.

    :ivar pos:
    :ivar point_property:
    :ivar point_rep: Deprecated with GML version 3.1.0. Use
        "pointProperty" instead. Included for backwards compatibility
        with GML 3.0.0.
    :ivar coord: Deprecated with GML version 3.0. Use "pos" instead. The
        "coord" element is included for backwards compatibility with GML
        2.
    :ivar pos_list:
    :ivar coordinates: Deprecated with GML version 3.1.0. Use "posList"
        instead.
    """
    pos: List[Pos] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 2,
            "sequential": True,
        }
    )
    point_property: List[PointProperty] = field(
        default_factory=list,
        metadata={
            "name": "pointProperty",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 2,
            "sequential": True,
        }
    )
    point_rep: List[PointRep] = field(
        default_factory=list,
        metadata={
            "name": "pointRep",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 2,
            "sequential": True,
        }
    )
    coord: List[Coord] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 2,
            "sequential": True,
        }
    )
    pos_list: Optional[PosList] = field(
        default=None,
        metadata={
            "name": "posList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    coordinates: Optional[Coordinates] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class LineString(LineStringType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class CurveArrayPropertyType:
    """A container for an array of curves.

    The elements are always contained in the array property, referencing
    geometry elements or arrays of geometry elements is not supported.
    """
    orientable_curve: List[OrientableCurve] = field(
        default_factory=list,
        metadata={
            "name": "OrientableCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    curve: List[Curve1] = field(
        default_factory=list,
        metadata={
            "name": "Curve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    composite_curve: List[CompositeCurve] = field(
        default_factory=list,
        metadata={
            "name": "CompositeCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    line_string: List[LineString] = field(
        default_factory=list,
        metadata={
            "name": "LineString",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    opengis_net_gml_curve: List[Curve2] = field(
        default_factory=list,
        metadata={
            "name": "_Curve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class CurvePropertyType:
    """A property that has a curve as its value domain can either be an
    appropriate geometry element encapsulated in an element of this type or an
    XLink reference to a remote geometry element (where remote includes
    geometry elements located elsewhere in the same document).

    Either the reference or the contained element must be given, but
    neither both nor none.
    """
    orientable_curve: Optional[OrientableCurve] = field(
        default=None,
        metadata={
            "name": "OrientableCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    curve: Optional[Curve1] = field(
        default=None,
        metadata={
            "name": "Curve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    composite_curve: Optional[CompositeCurve] = field(
        default=None,
        metadata={
            "name": "CompositeCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    line_string: Optional[LineString] = field(
        default=None,
        metadata={
            "name": "LineString",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    opengis_net_gml_curve: Optional[Curve2] = field(
        default=None,
        metadata={
            "name": "_Curve",
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
class GeometricPrimitivePropertyType:
    """A property that has a geometric primitive as its value domain can either
    be an appropriate geometry element encapsulated in an element of this type
    or an XLink reference to a remote geometry element (where remote includes
    geometry elements located elsewhere in the same document).

    Either the reference or the contained element must be given, but
    neither both nor none.
    """
    solid: Optional[Solid1] = field(
        default=None,
        metadata={
            "name": "Solid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    composite_solid: Optional[CompositeSolid] = field(
        default=None,
        metadata={
            "name": "CompositeSolid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    opengis_net_gml_solid: Optional[Solid2] = field(
        default=None,
        metadata={
            "name": "_Solid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    orientable_surface: Optional[OrientableSurface] = field(
        default=None,
        metadata={
            "name": "OrientableSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    tin: Optional[Tin] = field(
        default=None,
        metadata={
            "name": "Tin",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    triangulated_surface: Optional[TriangulatedSurface] = field(
        default=None,
        metadata={
            "name": "TriangulatedSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    polyhedral_surface: Optional[PolyhedralSurface] = field(
        default=None,
        metadata={
            "name": "PolyhedralSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    surface: Optional[Surface1] = field(
        default=None,
        metadata={
            "name": "Surface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    composite_surface: Optional[CompositeSurface] = field(
        default=None,
        metadata={
            "name": "CompositeSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    polygon: Optional[Polygon] = field(
        default=None,
        metadata={
            "name": "Polygon",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    opengis_net_gml_surface: Optional[Surface2] = field(
        default=None,
        metadata={
            "name": "_Surface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    orientable_curve: Optional[OrientableCurve] = field(
        default=None,
        metadata={
            "name": "OrientableCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    curve: Optional[Curve1] = field(
        default=None,
        metadata={
            "name": "Curve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    composite_curve: Optional[CompositeCurve] = field(
        default=None,
        metadata={
            "name": "CompositeCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    line_string: Optional[LineString] = field(
        default=None,
        metadata={
            "name": "LineString",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    opengis_net_gml_curve: Optional[Curve2] = field(
        default=None,
        metadata={
            "name": "_Curve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    point: Optional[Point] = field(
        default=None,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    geometric_primitive: Optional[GeometricPrimitive] = field(
        default=None,
        metadata={
            "name": "_GeometricPrimitive",
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
class GeometryArrayPropertyType:
    """A container for an array of geometry elements.

    The elements are always contained in the array property, referencing
    geometry elements or arrays of geometry elements is not supported.
    """
    multi_line_string: List[MultiLineString] = field(
        default_factory=list,
        metadata={
            "name": "MultiLineString",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    multi_polygon: List[MultiPolygon] = field(
        default_factory=list,
        metadata={
            "name": "MultiPolygon",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    multi_solid: List[MultiSolid] = field(
        default_factory=list,
        metadata={
            "name": "MultiSolid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    multi_surface: List[MultiSurface] = field(
        default_factory=list,
        metadata={
            "name": "MultiSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    multi_curve: List[MultiCurve] = field(
        default_factory=list,
        metadata={
            "name": "MultiCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    multi_point: List[MultiPoint] = field(
        default_factory=list,
        metadata={
            "name": "MultiPoint",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    multi_geometry: List["MultiGeometry"] = field(
        default_factory=list,
        metadata={
            "name": "MultiGeometry",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    geometric_aggregate: List[GeometricAggregate] = field(
        default_factory=list,
        metadata={
            "name": "_GeometricAggregate",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    rectified_grid: List[RectifiedGrid] = field(
        default_factory=list,
        metadata={
            "name": "RectifiedGrid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    grid: List[Grid] = field(
        default_factory=list,
        metadata={
            "name": "Grid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    implicit_geometry: List[ImplicitGeometry] = field(
        default_factory=list,
        metadata={
            "name": "_ImplicitGeometry",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    geometric_complex: List[GeometricComplex] = field(
        default_factory=list,
        metadata={
            "name": "GeometricComplex",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    ring: List[Ring1] = field(
        default_factory=list,
        metadata={
            "name": "Ring",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    linear_ring: List[LinearRing] = field(
        default_factory=list,
        metadata={
            "name": "LinearRing",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    opengis_net_gml_ring: List[Ring2] = field(
        default_factory=list,
        metadata={
            "name": "_Ring",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    solid: List[Solid1] = field(
        default_factory=list,
        metadata={
            "name": "Solid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    composite_solid: List[CompositeSolid] = field(
        default_factory=list,
        metadata={
            "name": "CompositeSolid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    opengis_net_gml_solid: List[Solid2] = field(
        default_factory=list,
        metadata={
            "name": "_Solid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    orientable_surface: List[OrientableSurface] = field(
        default_factory=list,
        metadata={
            "name": "OrientableSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    tin: List[Tin] = field(
        default_factory=list,
        metadata={
            "name": "Tin",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    triangulated_surface: List[TriangulatedSurface] = field(
        default_factory=list,
        metadata={
            "name": "TriangulatedSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    polyhedral_surface: List[PolyhedralSurface] = field(
        default_factory=list,
        metadata={
            "name": "PolyhedralSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    surface: List[Surface1] = field(
        default_factory=list,
        metadata={
            "name": "Surface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    composite_surface: List[CompositeSurface] = field(
        default_factory=list,
        metadata={
            "name": "CompositeSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    polygon: List[Polygon] = field(
        default_factory=list,
        metadata={
            "name": "Polygon",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    opengis_net_gml_surface: List[Surface2] = field(
        default_factory=list,
        metadata={
            "name": "_Surface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    orientable_curve: List[OrientableCurve] = field(
        default_factory=list,
        metadata={
            "name": "OrientableCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    curve: List[Curve1] = field(
        default_factory=list,
        metadata={
            "name": "Curve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    composite_curve: List[CompositeCurve] = field(
        default_factory=list,
        metadata={
            "name": "CompositeCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    line_string: List[LineString] = field(
        default_factory=list,
        metadata={
            "name": "LineString",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    opengis_net_gml_curve: List[Curve2] = field(
        default_factory=list,
        metadata={
            "name": "_Curve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    point: List[Point] = field(
        default_factory=list,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    geometric_primitive: List[GeometricPrimitive] = field(
        default_factory=list,
        metadata={
            "name": "_GeometricPrimitive",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    geometry: List[Geometry] = field(
        default_factory=list,
        metadata={
            "name": "_Geometry",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class GeometryPropertyType:
    """A geometric property can either be any geometry element encapsulated in
    an element of this type or an XLink reference to a remote geometry element
    (where remote includes geometry elements located elsewhere in the same
    document).

    Note that either the reference or the contained element must be
    given, but not both or none.
    """
    multi_line_string: Optional[MultiLineString] = field(
        default=None,
        metadata={
            "name": "MultiLineString",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    multi_polygon: Optional[MultiPolygon] = field(
        default=None,
        metadata={
            "name": "MultiPolygon",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    multi_solid: Optional[MultiSolid] = field(
        default=None,
        metadata={
            "name": "MultiSolid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    multi_surface: Optional[MultiSurface] = field(
        default=None,
        metadata={
            "name": "MultiSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    multi_curve: Optional[MultiCurve] = field(
        default=None,
        metadata={
            "name": "MultiCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    multi_point: Optional[MultiPoint] = field(
        default=None,
        metadata={
            "name": "MultiPoint",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    multi_geometry: Optional["MultiGeometry"] = field(
        default=None,
        metadata={
            "name": "MultiGeometry",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    geometric_aggregate: Optional[GeometricAggregate] = field(
        default=None,
        metadata={
            "name": "_GeometricAggregate",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    rectified_grid: Optional[RectifiedGrid] = field(
        default=None,
        metadata={
            "name": "RectifiedGrid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    grid: Optional[Grid] = field(
        default=None,
        metadata={
            "name": "Grid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    implicit_geometry: Optional[ImplicitGeometry] = field(
        default=None,
        metadata={
            "name": "_ImplicitGeometry",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    geometric_complex: Optional[GeometricComplex] = field(
        default=None,
        metadata={
            "name": "GeometricComplex",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    ring: Optional[Ring1] = field(
        default=None,
        metadata={
            "name": "Ring",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    linear_ring: Optional[LinearRing] = field(
        default=None,
        metadata={
            "name": "LinearRing",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    opengis_net_gml_ring: Optional[Ring2] = field(
        default=None,
        metadata={
            "name": "_Ring",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    solid: Optional[Solid1] = field(
        default=None,
        metadata={
            "name": "Solid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    composite_solid: Optional[CompositeSolid] = field(
        default=None,
        metadata={
            "name": "CompositeSolid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    opengis_net_gml_solid: Optional[Solid2] = field(
        default=None,
        metadata={
            "name": "_Solid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    orientable_surface: Optional[OrientableSurface] = field(
        default=None,
        metadata={
            "name": "OrientableSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    tin: Optional[Tin] = field(
        default=None,
        metadata={
            "name": "Tin",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    triangulated_surface: Optional[TriangulatedSurface] = field(
        default=None,
        metadata={
            "name": "TriangulatedSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    polyhedral_surface: Optional[PolyhedralSurface] = field(
        default=None,
        metadata={
            "name": "PolyhedralSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    surface: Optional[Surface1] = field(
        default=None,
        metadata={
            "name": "Surface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    composite_surface: Optional[CompositeSurface] = field(
        default=None,
        metadata={
            "name": "CompositeSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    polygon: Optional[Polygon] = field(
        default=None,
        metadata={
            "name": "Polygon",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    opengis_net_gml_surface: Optional[Surface2] = field(
        default=None,
        metadata={
            "name": "_Surface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    orientable_curve: Optional[OrientableCurve] = field(
        default=None,
        metadata={
            "name": "OrientableCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    curve: Optional[Curve1] = field(
        default=None,
        metadata={
            "name": "Curve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    composite_curve: Optional[CompositeCurve] = field(
        default=None,
        metadata={
            "name": "CompositeCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    line_string: Optional[LineString] = field(
        default=None,
        metadata={
            "name": "LineString",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    opengis_net_gml_curve: Optional[Curve2] = field(
        default=None,
        metadata={
            "name": "_Curve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    point: Optional[Point] = field(
        default=None,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    geometric_primitive: Optional[GeometricPrimitive] = field(
        default=None,
        metadata={
            "name": "_GeometricPrimitive",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    geometry: Optional[Geometry] = field(
        default=None,
        metadata={
            "name": "_Geometry",
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
class LineStringPropertyType:
    """This type is deprecated with GML 3 and shall not be used.

    It is included for backwards compatibility with GML 2. Use
    CurvePropertyType instead. A property that has a line string as its
    value domain can either be an appropriate geometry element
    encapsulated in an element of this type or an XLink reference to a
    remote geometry element (where remote includes geometry elements
    located elsewhere in the same document). Either the reference or the
    contained element must be given, but neither both nor none.
    """
    line_string: Optional[LineString] = field(
        default=None,
        metadata={
            "name": "LineString",
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
class CurveArrayProperty(CurveArrayPropertyType):
    class Meta:
        name = "curveArrayProperty"
        namespace = "http://www.opengis.net/gml"


@dataclass
class CurveProperty(CurvePropertyType):
    """This property element either references a curve via the XLink-attributes
    or contains the curve element.

    curveProperty is the predefined property which can be used by GML
    Application Schemas whenever a GML Feature has a property with a
    value that is substitutable for _Curve.
    """
    class Meta:
        name = "curveProperty"
        namespace = "http://www.opengis.net/gml"


@dataclass
class LineStringProperty(LineStringPropertyType):
    """Deprecated with GML 3.0 and included only for backwards compatibility
    with GML 2.0.

    Use "curveProperty" instead. This property element either references
    a line string via the XLink-attributes or contains the line string
    element.
    """
    class Meta:
        name = "lineStringProperty"
        namespace = "http://www.opengis.net/gml"
