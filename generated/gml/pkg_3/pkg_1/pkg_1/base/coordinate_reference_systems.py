from dataclasses import dataclass, field
from typing import List, Optional
from generated.gml.pkg_3.pkg_1.pkg_1.base.basic_types import CodeType
from generated.gml.pkg_3.pkg_1.pkg_1.base.coordinate_operations import GeneralConversionRefType
from generated.gml.pkg_3.pkg_1.pkg_1.base.coordinate_systems import (
    CartesianCsrefType,
    CoordinateSystemRefType,
    EllipsoidalCsrefType,
    ObliqueCartesianCsrefType,
    SphericalCsrefType,
    TemporalCsrefType,
    VerticalCsrefType,
)
from generated.gml.pkg_3.pkg_1.pkg_1.base.datums import (
    EngineeringDatumRefType,
    GeodeticDatumRefType,
    ImageDatumRefType,
    TemporalDatumRefType,
    VerticalDatumRefType,
)
from generated.gml.pkg_3.pkg_1.pkg_1.base.reference_systems import AbstractReferenceSystemType
from generated.xlink import (
    ActuateType,
    ShowType,
    TypeType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DerivedCrstypeType(CodeType):
    """
    Type of a derived coordinate reference system.
    """
    class Meta:
        name = "DerivedCRSTypeType"


@dataclass
class CoordinateReferenceSystem(AbstractReferenceSystemType):
    """A coordinate reference system consists of an ordered sequence of
    coordinate system axes that are related to the earth through a datum.

    A coordinate reference system is defined by one datum and by one
    coordinate system. Most coordinate reference system do not move
    relative to the earth, except for engineering coordinate reference
    systems defined on moving platforms such as cars, ships, aircraft,
    and spacecraft. For further information, see OGC Abstract
    Specification Topic 2. Coordinate reference systems are commonly
    divided into sub-types. The common classification criterion for sub-
    typing of coordinate reference systems is the way in which they deal
    with earth curvature. This has a direct effect on the portion of the
    earth's surface that can be covered by that type of CRS with an
    acceptable degree of error. The exception to the rule is the subtype
    "Temporal" which has been added by analogy.
    """
    class Meta:
        name = "_CoordinateReferenceSystem"
        namespace = "http://www.opengis.net/gml"


@dataclass
class DefinedByConversion(GeneralConversionRefType):
    """
    Association to the coordinate conversion used to define this derived CRS.
    """
    class Meta:
        name = "definedByConversion"
        namespace = "http://www.opengis.net/gml"


@dataclass
class UsesCs(CoordinateSystemRefType):
    """
    Association to the coordinate system used by this CRS.
    """
    class Meta:
        name = "usesCS"
        namespace = "http://www.opengis.net/gml"


@dataclass
class UsesCartesianCs(CartesianCsrefType):
    """
    Association to the Cartesian coordinate system used by this CRS.
    """
    class Meta:
        name = "usesCartesianCS"
        namespace = "http://www.opengis.net/gml"


@dataclass
class UsesEllipsoidalCs(EllipsoidalCsrefType):
    """
    Association to the ellipsoidal coordinate system used by this CRS.
    """
    class Meta:
        name = "usesEllipsoidalCS"
        namespace = "http://www.opengis.net/gml"


@dataclass
class UsesEngineeringDatum(EngineeringDatumRefType):
    """
    Association to the engineering datum used by this CRS.
    """
    class Meta:
        name = "usesEngineeringDatum"
        namespace = "http://www.opengis.net/gml"


@dataclass
class UsesGeodeticDatum(GeodeticDatumRefType):
    """
    Association to the geodetic datum used by this CRS.
    """
    class Meta:
        name = "usesGeodeticDatum"
        namespace = "http://www.opengis.net/gml"


@dataclass
class UsesImageDatum(ImageDatumRefType):
    """
    Association to the image datum used by this CRS.
    """
    class Meta:
        name = "usesImageDatum"
        namespace = "http://www.opengis.net/gml"


@dataclass
class UsesObliqueCartesianCs(ObliqueCartesianCsrefType):
    """
    Association to the oblique Cartesian coordinate system used by this CRS.
    """
    class Meta:
        name = "usesObliqueCartesianCS"
        namespace = "http://www.opengis.net/gml"


@dataclass
class UsesSphericalCs(SphericalCsrefType):
    """
    Association to the spherical coordinate system used by this CRS.
    """
    class Meta:
        name = "usesSphericalCS"
        namespace = "http://www.opengis.net/gml"


@dataclass
class UsesTemporalCs(TemporalCsrefType):
    """
    Association to the temporal coordinate system used by this CRS.
    """
    class Meta:
        name = "usesTemporalCS"
        namespace = "http://www.opengis.net/gml"


@dataclass
class UsesTemporalDatum(TemporalDatumRefType):
    """
    Association to the temporal datum used by this CRS.
    """
    class Meta:
        name = "usesTemporalDatum"
        namespace = "http://www.opengis.net/gml"


@dataclass
class UsesVerticalCs(VerticalCsrefType):
    """
    Association to the vertical coordinate system used by this CRS.
    """
    class Meta:
        name = "usesVerticalCS"
        namespace = "http://www.opengis.net/gml"


@dataclass
class UsesVerticalDatum(VerticalDatumRefType):
    """
    Association to the vertical datum used by this CRS.
    """
    class Meta:
        name = "usesVerticalDatum"
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
class EngineeringCrstype(AbstractReferenceSystemType):
    """A contextually local coordinate reference system; which can be divided
    into two broad categories:

    - earth-fixed systems applied to engineering activities on or near the surface of the earth;
    - CRSs on moving platforms such as road vehicles, vessels, aircraft, or spacecraft.
    For further information, see OGC Abstract Specification Topic 2.
    """
    class Meta:
        name = "EngineeringCRSType"

    uses_cs: Optional[UsesCs] = field(
        default=None,
        metadata={
            "name": "usesCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    uses_engineering_datum: Optional[UsesEngineeringDatum] = field(
        default=None,
        metadata={
            "name": "usesEngineeringDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )


@dataclass
class GeocentricCrstype(AbstractReferenceSystemType):
    """A 3D coordinate reference system with the origin at the approximate
    centre of mass of the earth.

    A geocentric CRS deals with the earth's curvature by taking a 3D
    spatial view, which obviates the need to model the earth's
    curvature.
    """
    class Meta:
        name = "GeocentricCRSType"

    uses_cartesian_cs: Optional[UsesCartesianCs] = field(
        default=None,
        metadata={
            "name": "usesCartesianCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    uses_spherical_cs: Optional[UsesSphericalCs] = field(
        default=None,
        metadata={
            "name": "usesSphericalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    uses_geodetic_datum: Optional[UsesGeodeticDatum] = field(
        default=None,
        metadata={
            "name": "usesGeodeticDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )


@dataclass
class GeographicCrstype(AbstractReferenceSystemType):
    """
    A coordinate reference system based on an ellipsoidal approximation of the
    geoid; this provides an accurate representation of the geometry of
    geographic features for a large portion of the earth's surface.
    """
    class Meta:
        name = "GeographicCRSType"

    uses_ellipsoidal_cs: Optional[UsesEllipsoidalCs] = field(
        default=None,
        metadata={
            "name": "usesEllipsoidalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    uses_geodetic_datum: Optional[UsesGeodeticDatum] = field(
        default=None,
        metadata={
            "name": "usesGeodeticDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )


@dataclass
class ImageCrstype(AbstractReferenceSystemType):
    """An engineering coordinate reference system applied to locations in
    images.

    Image coordinate reference systems are treated as a separate sub-
    type because a separate user community exists for images with its
    own terms of reference.
    """
    class Meta:
        name = "ImageCRSType"

    uses_cartesian_cs: Optional[UsesCartesianCs] = field(
        default=None,
        metadata={
            "name": "usesCartesianCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    uses_oblique_cartesian_cs: Optional[UsesObliqueCartesianCs] = field(
        default=None,
        metadata={
            "name": "usesObliqueCartesianCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    uses_image_datum: Optional[UsesImageDatum] = field(
        default=None,
        metadata={
            "name": "usesImageDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )


@dataclass
class TemporalCrstype(AbstractReferenceSystemType):
    """
    A 1D coordinate reference system used for the recording of time.
    """
    class Meta:
        name = "TemporalCRSType"

    uses_temporal_cs: Optional[UsesTemporalCs] = field(
        default=None,
        metadata={
            "name": "usesTemporalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    uses_temporal_datum: Optional[UsesTemporalDatum] = field(
        default=None,
        metadata={
            "name": "usesTemporalDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )


@dataclass
class VerticalCrstype(AbstractReferenceSystemType):
    """A 1D coordinate reference system used for recording heights or depths.

    Vertical CRSs make use of the direction of gravity to define the
    concept of height or depth, but the relationship with gravity may
    not be straightforward. By implication, ellipsoidal heights (h)
    cannot be captured in a vertical coordinate reference system.
    Ellipsoidal heights cannot exist independently, but only as an
    inseparable part of a 3D coordinate tuple defined in a geographic 3D
    coordinate reference system.
    """
    class Meta:
        name = "VerticalCRSType"

    uses_vertical_cs: Optional[UsesVerticalCs] = field(
        default=None,
        metadata={
            "name": "usesVerticalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    uses_vertical_datum: Optional[UsesVerticalDatum] = field(
        default=None,
        metadata={
            "name": "usesVerticalDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )


@dataclass
class DerivedCrstype(DerivedCrstypeType):
    class Meta:
        name = "derivedCRSType"
        namespace = "http://www.opengis.net/gml"


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
class EngineeringCrs(EngineeringCrstype):
    class Meta:
        name = "EngineeringCRS"
        namespace = "http://www.opengis.net/gml"


@dataclass
class GeocentricCrs(GeocentricCrstype):
    class Meta:
        name = "GeocentricCRS"
        namespace = "http://www.opengis.net/gml"


@dataclass
class GeographicCrs(GeographicCrstype):
    class Meta:
        name = "GeographicCRS"
        namespace = "http://www.opengis.net/gml"


@dataclass
class ImageCrs(ImageCrstype):
    class Meta:
        name = "ImageCRS"
        namespace = "http://www.opengis.net/gml"


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
class TemporalCrs(TemporalCrstype):
    class Meta:
        name = "TemporalCRS"
        namespace = "http://www.opengis.net/gml"


@dataclass
class VerticalCrs(VerticalCrstype):
    class Meta:
        name = "VerticalCRS"
        namespace = "http://www.opengis.net/gml"


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
class EngineeringCrsrefType:
    """
    Association to an engineering coordinate reference system, either
    referencing or containing the definition of that reference system.
    """
    class Meta:
        name = "EngineeringCRSRefType"

    engineering_crs: Optional[EngineeringCrs] = field(
        default=None,
        metadata={
            "name": "EngineeringCRS",
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
class GeocentricCrsrefType:
    """
    Association to a geocentric coordinate reference system, either referencing
    or containing the definition of that reference system.
    """
    class Meta:
        name = "GeocentricCRSRefType"

    geocentric_crs: Optional[GeocentricCrs] = field(
        default=None,
        metadata={
            "name": "GeocentricCRS",
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
class GeographicCrsrefType:
    """
    Association to a geographic coordinate reference system, either referencing
    or containing the definition of that reference system.
    """
    class Meta:
        name = "GeographicCRSRefType"

    geographic_crs: Optional[GeographicCrs] = field(
        default=None,
        metadata={
            "name": "GeographicCRS",
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
class ImageCrsrefType:
    """
    Association to an image coordinate reference system, either referencing or
    containing the definition of that reference system.
    """
    class Meta:
        name = "ImageCRSRefType"

    image_crs: Optional[ImageCrs] = field(
        default=None,
        metadata={
            "name": "ImageCRS",
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
class ProjectedCrs(ProjectedCrstype):
    class Meta:
        name = "ProjectedCRS"
        namespace = "http://www.opengis.net/gml"


@dataclass
class TemporalCrsrefType:
    """
    Association to a temporal coordinate reference system, either referencing
    or containing the definition of that reference system.
    """
    class Meta:
        name = "TemporalCRSRefType"

    temporal_crs: Optional[TemporalCrs] = field(
        default=None,
        metadata={
            "name": "TemporalCRS",
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
class VerticalCrsrefType:
    """
    Association to a vertical coordinate reference system, either referencing
    or containing the definition of that reference system.
    """
    class Meta:
        name = "VerticalCRSRefType"

    vertical_crs: Optional[VerticalCrs] = field(
        default=None,
        metadata={
            "name": "VerticalCRS",
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
class DerivedCrsrefType:
    """
    Association to a non-projected derived coordinate reference system, either
    referencing or containing the definition of that reference system.
    """
    class Meta:
        name = "DerivedCRSRefType"

    derived_crs: Optional[DerivedCrs] = field(
        default=None,
        metadata={
            "name": "DerivedCRS",
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
class ProjectedCrsrefType:
    """
    Association to a projected coordinate reference system, either referencing
    or containing the definition of that reference system.
    """
    class Meta:
        name = "ProjectedCRSRefType"

    projected_crs: Optional[ProjectedCrs] = field(
        default=None,
        metadata={
            "name": "ProjectedCRS",
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
class EngineeringCrsref(EngineeringCrsrefType):
    class Meta:
        name = "engineeringCRSRef"
        namespace = "http://www.opengis.net/gml"


@dataclass
class GeocentricCrsref(GeocentricCrsrefType):
    class Meta:
        name = "geocentricCRSRef"
        namespace = "http://www.opengis.net/gml"


@dataclass
class GeographicCrsref(GeographicCrsrefType):
    class Meta:
        name = "geographicCRSRef"
        namespace = "http://www.opengis.net/gml"


@dataclass
class ImageCrsref(ImageCrsrefType):
    class Meta:
        name = "imageCRSRef"
        namespace = "http://www.opengis.net/gml"


@dataclass
class TemporalCrsref(TemporalCrsrefType):
    class Meta:
        name = "temporalCRSRef"
        namespace = "http://www.opengis.net/gml"


@dataclass
class VerticalCrsref(VerticalCrsrefType):
    class Meta:
        name = "verticalCRSRef"
        namespace = "http://www.opengis.net/gml"


@dataclass
class BaseCrs(CoordinateReferenceSystemRefType):
    """
    Association to the coordinate reference system used by this derived CRS.
    """
    class Meta:
        name = "baseCRS"
        namespace = "http://www.opengis.net/gml"


@dataclass
class CoordinateReferenceSystemRef(CoordinateReferenceSystemRefType):
    class Meta:
        name = "coordinateReferenceSystemRef"
        namespace = "http://www.opengis.net/gml"


@dataclass
class DerivedCrsref(DerivedCrsrefType):
    class Meta:
        name = "derivedCRSRef"
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
class ProjectedCrsref(ProjectedCrsrefType):
    class Meta:
        name = "projectedCRSRef"
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
class CompoundCrsrefType:
    """
    Association to a compound coordinate reference system, either referencing
    or containing the definition of that reference system.
    """
    class Meta:
        name = "CompoundCRSRefType"

    compound_crs: Optional[CompoundCrs] = field(
        default=None,
        metadata={
            "name": "CompoundCRS",
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
class CompoundCrsref(CompoundCrsrefType):
    class Meta:
        name = "compoundCRSRef"
        namespace = "http://www.opengis.net/gml"
