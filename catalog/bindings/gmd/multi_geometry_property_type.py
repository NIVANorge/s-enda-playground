from dataclasses import dataclass, field
from typing import Optional, Union
from bindings.gmd.abstract_geometric_aggregate import AbstractGeometricAggregate
from bindings.gmd.actuate_value import ActuateValue
from bindings.gmd.geometry_array_property_type import MultiGeometry
from bindings.gmd.multi_curve import MultiCurve
from bindings.gmd.multi_point import MultiPoint
from bindings.gmd.multi_solid import MultiSolid
from bindings.gmd.multi_surface import MultiSurface
from bindings.gmd.nil_reason_enumeration_value import NilReasonEnumerationValue
from bindings.gmd.show_value import ShowValue

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MultiGeometryPropertyType:
    """A property that has a geometric aggregate as its value domain may either
    be an appropriate geometry element encapsulated in an element of this type
    or an XLink reference to a remote geometry element (where remote includes
    geometry elements located elsewhere in the same document).

    Either the reference or the contained element shall be given, but
    neither both nor none.
    """

    multi_solid: Optional[MultiSolid] = field(
        default=None,
        metadata={
            "name": "MultiSolid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_surface: Optional[MultiSurface] = field(
        default=None,
        metadata={
            "name": "MultiSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_curve: Optional[MultiCurve] = field(
        default=None,
        metadata={
            "name": "MultiCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_point: Optional[MultiPoint] = field(
        default=None,
        metadata={
            "name": "MultiPoint",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_geometry: Optional[MultiGeometry] = field(
        default=None,
        metadata={
            "name": "MultiGeometry",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    abstract_geometric_aggregate: Optional[AbstractGeometricAggregate] = field(
        default=None,
        metadata={
            "name": "AbstractGeometricAggregate",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    type: str = field(
        init=False,
        default="simple",
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
        },
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    show: Optional[ShowValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    actuate: Optional[ActuateValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:\w{2,}",
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
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
