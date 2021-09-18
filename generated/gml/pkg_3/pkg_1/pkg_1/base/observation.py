from dataclasses import dataclass, field
from typing import Optional
from generated.gml.pkg_3.pkg_1.pkg_1.base.basic_types import MeasureType
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
from generated.gml.pkg_3.pkg_1.pkg_1.base.direction import Direction
from generated.gml.pkg_3.pkg_1.pkg_1.base.feature import (
    AbstractFeatureType,
    FeatureCollection1,
    FeaturePropertyType,
    Feature,
    FeatureCollection2,
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
    LineString,
    Point,
    Curve2,
    GeometricPrimitive,
    Geometry,
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
from generated.gml.pkg_3.pkg_1.pkg_1.base.gml_base import AssociationType
from generated.gml.pkg_3.pkg_1.pkg_1.base.grids import (
    Grid,
    RectifiedGrid,
    ImplicitGeometry,
)
from generated.gml.pkg_3.pkg_1.pkg_1.base.temporal import ValidTime
from generated.xlink import (
    ActuateType,
    ShowType,
    TypeType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TargetPropertyType:
    """
    Container for an object representing the target or subject of an
    observation.
    """
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
class ResultOf(AssociationType):
    """
    The result of the observation: an image, external object, etc.
    """
    class Meta:
        name = "resultOf"
        namespace = "http://www.opengis.net/gml"


@dataclass
class Using(FeaturePropertyType):
    """
    This element contains or points to a description of a sensor, instrument or
    procedure used for the observation.
    """
    class Meta:
        name = "using"
        namespace = "http://www.opengis.net/gml"


@dataclass
class Subject(TargetPropertyType):
    """Synonym for target - common word used for photographs"""
    class Meta:
        name = "subject"
        namespace = "http://www.opengis.net/gml"


@dataclass
class Target(TargetPropertyType):
    """
    This element contains or points to the specimen, region or station which is
    the object of the observation.
    """
    class Meta:
        name = "target"
        namespace = "http://www.opengis.net/gml"


@dataclass
class ObservationType(AbstractFeatureType):
    valid_time: Optional[ValidTime] = field(
        default=None,
        metadata={
            "name": "validTime",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    using: Optional[Using] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    subject: Optional[Subject] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    target: Optional[Target] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    result_of: Optional["ResultOf"] = field(
        default=None,
        metadata={
            "name": "resultOf",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )


@dataclass
class DirectedObservationType(ObservationType):
    direction: Optional[Direction] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )


@dataclass
class Observation(ObservationType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class DirectedObservation(DirectedObservationType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class DirectedObservationAtDistanceType(DirectedObservationType):
    distance: Optional[MeasureType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )


@dataclass
class DirectedObservationAtDistance(DirectedObservationAtDistanceType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
