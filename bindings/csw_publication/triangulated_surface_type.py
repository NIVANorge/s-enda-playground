from dataclasses import dataclass, field
from typing import List
from bindings.csw_publication.srs_name import SrsName
from bindings.csw_publication.surface_type import SurfaceType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TriangulatedSurfaceType(SurfaceType):
    """A triangulated surface is a polyhedral surface that is composed only of
    triangles.

    There is no restriction on how the triangulation is derived.
    """
    srs_name: List[SrsName] = field(
        default_factory=list,
        metadata={
            "name": "srsName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
