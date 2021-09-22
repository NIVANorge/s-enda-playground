from dataclasses import dataclass, field
from typing import Optional
from bindings.csw_publication.inverse_flattening import InverseFlattening
from bindings.csw_publication.is_sphere_value import IsSphereValue
from bindings.csw_publication.semi_minor_axis import SemiMinorAxis

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class SecondDefiningParameterType:
    """Definition of the second parameter that defines the shape of an
    ellipsoid.

    An ellipsoid requires two defining parameters: semi-major axis and
    inverse flattening or semi-major axis and semi-minor axis. When the
    reference body is a sphere rather than an ellipsoid, only a single
    defining parameter is required, namely the radius of the sphere; in
    that case, the semi-major axis "degenerates" into the radius of the
    sphere.
    """
    inverse_flattening: Optional[InverseFlattening] = field(
        default=None,
        metadata={
            "name": "inverseFlattening",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    semi_minor_axis: Optional[SemiMinorAxis] = field(
        default=None,
        metadata={
            "name": "semiMinorAxis",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    is_sphere: Optional[IsSphereValue] = field(
        default=None,
        metadata={
            "name": "isSphere",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
