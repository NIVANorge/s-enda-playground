from dataclasses import dataclass, field
from typing import List, Optional
from bindings.csw.abstract_surface_type import AbstractSurfaceType
from bindings.csw.actuate_type import ActuateType
from bindings.csw.polygon import Polygon
from bindings.csw.polyhedral_surface import PolyhedralSurface
from bindings.csw.show_type import ShowType
from bindings.csw.sign_type import SignType
from bindings.csw.surface_1 import Surface1
from bindings.csw.surface_2 import Surface2
from bindings.csw.tin import Tin
from bindings.csw.triangulated_surface import TriangulatedSurface
from bindings.csw.type_type import TypeType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CompositeSurfaceType(AbstractSurfaceType):
    """A CompositeSurface is defined by a set of orientable surfaces.

    A composite surface is geometry type with all the geometric
    properties of a (primitive) surface. Essentially, a composite
    surface is a collection of surfaces that join in pairs on common
    boundary curves and which, when considered as a whole, form a single
    surface.

    :ivar surface_member: This element references or contains one
        surface in the composite surface. The surfaces are contiguous.
        NOTE: This definition allows for a nested structure, i.e. a
        CompositeSurface may use, for example, another CompositeSurface
        as a member.
    """

    surface_member: List["SurfaceMember"] = field(
        default_factory=list,
        metadata={
            "name": "surfaceMember",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        },
    )


@dataclass
class OrientableSurfaceType(AbstractSurfaceType):
    """OrientableSurface consists of a surface and an orientation.

    If the orientation is "+", then the OrientableSurface is identical
    to the baseSurface. If the orientation is "-", then the
    OrientableSurface is a reference to a Surface with an up-normal that
    reverses the direction for this OrientableSurface, the sense of "the
    top of the surface".

    :ivar base_surface: References or contains the base surface
        (positive orientation).
    :ivar orientation: If the orientation is "+", then the
        OrientableSurface is identical to the baseSurface. If the
        orientation is "-", then the OrientableSurface is a reference to
        a Surface with an up-normal that reverses the direction for this
        OrientableSurface, the sense of "the top of the surface". "+" is
        the default value.
    """

    base_surface: Optional["BaseSurface"] = field(
        default=None,
        metadata={
            "name": "baseSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    orientation: SignType = field(
        default=SignType.VALUE,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class CompositeSurface(CompositeSurfaceType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class OrientableSurface(OrientableSurfaceType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class SurfacePropertyType:
    """A property that has a surface as its value domain can either be an
    appropriate geometry element encapsulated in an element of this type or an
    XLink reference to a remote geometry element (where remote includes
    geometry elements located elsewhere in the same document).

    Either the reference or the contained element must be given, but
    neither both nor none.
    """

    orientable_surface: Optional[OrientableSurface] = field(
        default=None,
        metadata={
            "name": "OrientableSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    tin: Optional[Tin] = field(
        default=None,
        metadata={
            "name": "Tin",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    triangulated_surface: Optional[TriangulatedSurface] = field(
        default=None,
        metadata={
            "name": "TriangulatedSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    polyhedral_surface: Optional[PolyhedralSurface] = field(
        default=None,
        metadata={
            "name": "PolyhedralSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    surface: Optional[Surface1] = field(
        default=None,
        metadata={
            "name": "Surface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    composite_surface: Optional[CompositeSurface] = field(
        default=None,
        metadata={
            "name": "CompositeSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    polygon: Optional[Polygon] = field(
        default=None,
        metadata={
            "name": "Polygon",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    opengis_net_gml_surface: Optional[Surface2] = field(
        default=None,
        metadata={
            "name": "_Surface",
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


@dataclass
class BaseSurface(SurfacePropertyType):
    """This property element either references a surface via the XLink-
    attributes or contains the surface element.

    A surface element is any element which is substitutable for
    "_Surface".
    """

    class Meta:
        name = "baseSurface"
        namespace = "http://www.opengis.net/gml"


@dataclass
class SurfaceMember(SurfacePropertyType):
    """This property element either references a surface via the XLink-
    attributes or contains the surface element.

    A surface element is any element which is substitutable for
    "_Surface".
    """

    class Meta:
        name = "surfaceMember"
        namespace = "http://www.opengis.net/gml"
