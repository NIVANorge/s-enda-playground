from dataclasses import dataclass, field
from typing import Optional
from bindings.gmd.greenwich_longitude import GreenwichLongitude
from bindings.gmd.identified_object_type import IdentifiedObjectType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class PrimeMeridianType(IdentifiedObjectType):
    greenwich_longitude: Optional[GreenwichLongitude] = field(
        default=None,
        metadata={
            "name": "greenwichLongitude",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
