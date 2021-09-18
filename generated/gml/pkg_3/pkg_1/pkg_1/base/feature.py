from dataclasses import dataclass, field
from typing import List, Optional, Union
from generated.gml.pkg_3.pkg_1.pkg_1.base.basic_types import (
    CodeType,
    NullEnumerationValue,
)
from generated.gml.pkg_3.pkg_1.pkg_1.base.coverage import (
    GridCoverage,
    MultiCurveCoverage,
    MultiPointCoverage,
    MultiSolidCoverage,
    MultiSurfaceCoverage,
    RectifiedGridCoverage,
    ContinuousCoverage,
    Coverage,
    DiscreteCoverage,
)
from generated.gml.pkg_3.pkg_1.pkg_1.base.geometry_aggregates import (
    MultiCurve,
    MultiGeometry,
    MultiLineString,
    MultiPoint,
    MultiPolygon,
    MultiSolid,
    MultiSurface,
    GeometricAggregate,
)
from generated.gml.pkg_3.pkg_1.pkg_1.base.geometry_basic0d1d import (
    CurvePropertyType,
    Envelope,
    EnvelopeType,
    LineString,
    Point,
    PointPropertyType,
    Curve2,
    GeometricPrimitive,
    Geometry,
)
from generated.gml.pkg_3.pkg_1.pkg_1.base.geometry_basic2d import (
    LinearRing,
    Polygon,
    SurfacePropertyType,
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
    AbstractGmltype,
    StringOrRefType,
)
from generated.gml.pkg_3.pkg_1.pkg_1.base.grids import (
    Grid,
    RectifiedGrid,
    ImplicitGeometry,
)
from generated.gml.pkg_3.pkg_1.pkg_1.base.temporal import TimePosition
from generated.xlink import (
    ActuateType,
    ShowType,
    TypeType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class EnvelopeWithTimePeriodType(EnvelopeType):
    """
    Envelope that includes also a temporal extent.
    """
    time_position: List[TimePosition] = field(
        default_factory=list,
        metadata={
            "name": "timePosition",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 2,
            "max_occurs": 2,
        }
    )
    frame: str = field(
        default="#ISO-8601",
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class LocationKeyWord(CodeType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class LocationString(StringOrRefType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class CenterLineOf(CurvePropertyType):
    class Meta:
        name = "centerLineOf"
        namespace = "http://www.opengis.net/gml"


@dataclass
class CenterOf(PointPropertyType):
    class Meta:
        name = "centerOf"
        namespace = "http://www.opengis.net/gml"


@dataclass
class EdgeOf(CurvePropertyType):
    class Meta:
        name = "edgeOf"
        namespace = "http://www.opengis.net/gml"


@dataclass
class ExtentOf(SurfacePropertyType):
    class Meta:
        name = "extentOf"
        namespace = "http://www.opengis.net/gml"


@dataclass
class Position(PointPropertyType):
    class Meta:
        name = "position"
        namespace = "http://www.opengis.net/gml"


@dataclass
class EnvelopeWithTimePeriod(EnvelopeWithTimePeriodType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class LocationPropertyType:
    """Convenience property for generalised location.

    A representative location for plotting or analysis. Often augmented
    by one or more additional geometry properties with more specific
    semantics. Deprecated in GML 3.1.0
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
    multi_geometry: Optional[MultiGeometry] = field(
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
    location_key_word: Optional[LocationKeyWord] = field(
        default=None,
        metadata={
            "name": "LocationKeyWord",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    location_string: Optional[LocationString] = field(
        default=None,
        metadata={
            "name": "LocationString",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    null: Optional[Union[str, NullEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "Null",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "pattern": r"other:\w{2,}",
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
class BoundingShapeType:
    """
    Bounding shape.
    """
    envelope_with_time_period: Optional[EnvelopeWithTimePeriod] = field(
        default=None,
        metadata={
            "name": "EnvelopeWithTimePeriod",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    envelope: Optional[Envelope] = field(
        default=None,
        metadata={
            "name": "Envelope",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    null: Optional[Union[str, NullEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "Null",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "pattern": r"other:\w{2,}",
        }
    )


@dataclass
class PriorityLocationPropertyType(LocationPropertyType):
    """
    G-XML component Deprecated in GML 3.1.0.
    """
    priority: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Location(LocationPropertyType):
    """
    Deprecated in GML 3.1.0.
    """
    class Meta:
        name = "location"
        namespace = "http://www.opengis.net/gml"


@dataclass
class BoundedBy(BoundingShapeType):
    class Meta:
        name = "boundedBy"
        namespace = "http://www.opengis.net/gml"


@dataclass
class PriorityLocation(PriorityLocationPropertyType):
    """
    Deprecated in GML 3.1.0.
    """
    class Meta:
        name = "priorityLocation"
        namespace = "http://www.opengis.net/gml"


@dataclass
class AbstractFeatureType(AbstractGmltype):
    """An abstract feature provides a set of common properties, including id,
    metaDataProperty, name and description inherited from AbstractGMLType, plus
    boundedBy.

    A concrete feature type must derive from this type and specify additional  properties in an application schema. A feature must possess an identifying attribute ('id' - 'fid' has been deprecated).

    :ivar bounded_by:
    :ivar priority_location:
    :ivar location: deprecated in GML version 3.1
    """
    bounded_by: Optional[BoundedBy] = field(
        default=None,
        metadata={
            "name": "boundedBy",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    priority_location: Optional[PriorityLocation] = field(
        default=None,
        metadata={
            "name": "priorityLocation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    location: Optional[Location] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class BoundedFeatureType(AbstractFeatureType):
    """
    Makes boundedBy mandatory.
    """


@dataclass
class Feature(AbstractFeatureType):
    class Meta:
        name = "_Feature"
        namespace = "http://www.opengis.net/gml"


@dataclass
class FeatureArrayPropertyType:
    """Container for features - follow gml:ArrayAssociationType pattern."""
    directed_observation_at_distance: List["DirectedObservationAtDistance"] = field(
        default_factory=list,
        metadata={
            "name": "DirectedObservationAtDistance",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    directed_observation: List["DirectedObservation"] = field(
        default_factory=list,
        metadata={
            "name": "DirectedObservation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    observation: List["Observation"] = field(
        default_factory=list,
        metadata={
            "name": "Observation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    rectified_grid_coverage: List["RectifiedGridCoverage"] = field(
        default_factory=list,
        metadata={
            "name": "RectifiedGridCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    grid_coverage: List["GridCoverage"] = field(
        default_factory=list,
        metadata={
            "name": "GridCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    multi_solid_coverage: List["MultiSolidCoverage"] = field(
        default_factory=list,
        metadata={
            "name": "MultiSolidCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    multi_surface_coverage: List["MultiSurfaceCoverage"] = field(
        default_factory=list,
        metadata={
            "name": "MultiSurfaceCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    multi_curve_coverage: List["MultiCurveCoverage"] = field(
        default_factory=list,
        metadata={
            "name": "MultiCurveCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    multi_point_coverage: List["MultiPointCoverage"] = field(
        default_factory=list,
        metadata={
            "name": "MultiPointCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    discrete_coverage: List["DiscreteCoverage"] = field(
        default_factory=list,
        metadata={
            "name": "_DiscreteCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    continuous_coverage: List["ContinuousCoverage"] = field(
        default_factory=list,
        metadata={
            "name": "_ContinuousCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    coverage: List["Coverage"] = field(
        default_factory=list,
        metadata={
            "name": "_Coverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    feature_collection: List["FeatureCollection1"] = field(
        default_factory=list,
        metadata={
            "name": "FeatureCollection",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    opengis_net_gml_feature_collection: List["FeatureCollection2"] = field(
        default_factory=list,
        metadata={
            "name": "_FeatureCollection",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    feature: List[Feature] = field(
        default_factory=list,
        metadata={
            "name": "_Feature",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class FeatureMembers(FeatureArrayPropertyType):
    class Meta:
        name = "featureMembers"
        namespace = "http://www.opengis.net/gml"


@dataclass
class AbstractFeatureCollectionType(AbstractFeatureType):
    """
    A feature collection contains zero or more features.
    """
    feature_member: List["FeatureMember"] = field(
        default_factory=list,
        metadata={
            "name": "featureMember",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    feature_members: Optional[FeatureMembers] = field(
        default=None,
        metadata={
            "name": "featureMembers",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class FeatureCollectionType(AbstractFeatureCollectionType):
    """
    Concrete generic feature collection.
    """


@dataclass
class FeatureCollection2(AbstractFeatureCollectionType):
    class Meta:
        name = "_FeatureCollection"
        namespace = "http://www.opengis.net/gml"


@dataclass
class FeatureCollection1(FeatureCollectionType):
    class Meta:
        name = "FeatureCollection"
        namespace = "http://www.opengis.net/gml"


@dataclass
class FeaturePropertyType:
    """Container for a feature - follow gml:AssociationType pattern."""
    directed_observation_at_distance: Optional["DirectedObservationAtDistance"] = field(
        default=None,
        metadata={
            "name": "DirectedObservationAtDistance",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    directed_observation: Optional["DirectedObservation"] = field(
        default=None,
        metadata={
            "name": "DirectedObservation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    observation: Optional["Observation"] = field(
        default=None,
        metadata={
            "name": "Observation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    rectified_grid_coverage: Optional[RectifiedGridCoverage] = field(
        default=None,
        metadata={
            "name": "RectifiedGridCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    grid_coverage: Optional[GridCoverage] = field(
        default=None,
        metadata={
            "name": "GridCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    multi_solid_coverage: Optional[MultiSolidCoverage] = field(
        default=None,
        metadata={
            "name": "MultiSolidCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    multi_surface_coverage: Optional[MultiSurfaceCoverage] = field(
        default=None,
        metadata={
            "name": "MultiSurfaceCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    multi_curve_coverage: Optional[MultiCurveCoverage] = field(
        default=None,
        metadata={
            "name": "MultiCurveCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    multi_point_coverage: Optional[MultiPointCoverage] = field(
        default=None,
        metadata={
            "name": "MultiPointCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    discrete_coverage: Optional[DiscreteCoverage] = field(
        default=None,
        metadata={
            "name": "_DiscreteCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    continuous_coverage: Optional[ContinuousCoverage] = field(
        default=None,
        metadata={
            "name": "_ContinuousCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    coverage: Optional[Coverage] = field(
        default=None,
        metadata={
            "name": "_Coverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    feature_collection: Optional[FeatureCollection1] = field(
        default=None,
        metadata={
            "name": "FeatureCollection",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    opengis_net_gml_feature_collection: Optional[FeatureCollection2] = field(
        default=None,
        metadata={
            "name": "_FeatureCollection",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    feature: Optional[Feature] = field(
        default=None,
        metadata={
            "name": "_Feature",
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
class FeatureMember(FeaturePropertyType):
    class Meta:
        name = "featureMember"
        namespace = "http://www.opengis.net/gml"


@dataclass
class FeatureProperty(FeaturePropertyType):
    class Meta:
        name = "featureProperty"
        namespace = "http://www.opengis.net/gml"
