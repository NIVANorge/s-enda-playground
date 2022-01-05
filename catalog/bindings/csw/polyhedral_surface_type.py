from dataclasses import dataclass, field
from typing import List
from bindings.csw.srs_name import SrsName
from bindings.csw.surface_type import SurfaceType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class PolyhedralSurfaceType(SurfaceType):
    """A polyhedral surface is a surface composed of polygon surfaces connected
    along their common boundary curves.

    This differs from the surface type only in the restriction on the
    types of surface patches acceptable.
    """
    srs_name: List[SrsName] = field(
        default_factory=list,
        metadata={
            "name": "srsName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
