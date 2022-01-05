from dataclasses import dataclass, field
from typing import Optional
from bindings.csw.topo_curve import TopoCurve

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TopoCurvePropertyType:
    topo_curve: Optional[TopoCurve] = field(
        default=None,
        metadata={
            "name": "TopoCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
