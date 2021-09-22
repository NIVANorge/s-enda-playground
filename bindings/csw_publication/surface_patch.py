from dataclasses import dataclass
from bindings.csw_publication.abstract_surface_patch_type import AbstractSurfacePatchType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class SurfacePatch(AbstractSurfacePatchType):
    """
    The "_SurfacePatch" element is the abstract head of the substituition group
    for all surface pach elements describing a continuous portion of a surface.
    """
    class Meta:
        name = "_SurfacePatch"
        namespace = "http://www.opengis.net/gml"
