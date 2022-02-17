from dataclasses import dataclass, field
from typing import Optional
from bindings.gmd.topo_surface import TopoSurface

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TopoSurfacePropertyType:
    topo_surface: Optional[TopoSurface] = field(
        default=None,
        metadata={
            "name": "TopoSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
