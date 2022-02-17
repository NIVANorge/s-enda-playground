from dataclasses import dataclass, field
from typing import Optional
from bindings.csw.actuate_type import ActuateType
from bindings.csw.coordinate_reference_system import CoordinateReferenceSystem
from bindings.csw.crs import Crs
from bindings.csw.engineering_crs import EngineeringCrs
from bindings.csw.general_conversion_ref_type import (
    CompoundCrs,
    DerivedCrs,
    ProjectedCrs,
    GeneralDerivedCrs,
)
from bindings.csw.geocentric_crs import GeocentricCrs
from bindings.csw.geographic_crs import GeographicCrs
from bindings.csw.image_crs import ImageCrs
from bindings.csw.reference_system import ReferenceSystem
from bindings.csw.show_type import ShowType
from bindings.csw.temporal_crs import TemporalCrs
from bindings.csw.type_type import TypeType
from bindings.csw.vertical_crs import VerticalCrs

__NAMESPACE__ = "http://www.opengis.net/gml"


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
        },
    )
    temporal_crs: Optional[TemporalCrs] = field(
        default=None,
        metadata={
            "name": "TemporalCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    image_crs: Optional[ImageCrs] = field(
        default=None,
        metadata={
            "name": "ImageCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    engineering_crs: Optional[EngineeringCrs] = field(
        default=None,
        metadata={
            "name": "EngineeringCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    derived_crs: Optional[DerivedCrs] = field(
        default=None,
        metadata={
            "name": "DerivedCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    projected_crs: Optional[ProjectedCrs] = field(
        default=None,
        metadata={
            "name": "ProjectedCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    general_derived_crs: Optional[GeneralDerivedCrs] = field(
        default=None,
        metadata={
            "name": "_GeneralDerivedCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    geocentric_crs: Optional[GeocentricCrs] = field(
        default=None,
        metadata={
            "name": "GeocentricCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    vertical_crs: Optional[VerticalCrs] = field(
        default=None,
        metadata={
            "name": "VerticalCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    geographic_crs: Optional[GeographicCrs] = field(
        default=None,
        metadata={
            "name": "GeographicCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    coordinate_reference_system: Optional[CoordinateReferenceSystem] = field(
        default=None,
        metadata={
            "name": "_CoordinateReferenceSystem",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    crs: Optional[Crs] = field(
        default=None,
        metadata={
            "name": "_CRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    reference_system: Optional[ReferenceSystem] = field(
        default=None,
        metadata={
            "name": "_ReferenceSystem",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    type: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    remote_schema: Optional[str] = field(
        default=None,
        metadata={
            "name": "remoteSchema",
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml",
        },
    )
