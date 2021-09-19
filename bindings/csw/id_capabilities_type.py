from dataclasses import dataclass, field
from typing import List
from bindings.csw.eid import Eid
from bindings.csw.fid import Fid

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class IdCapabilitiesType:
    class Meta:
        name = "Id_CapabilitiesType"

    eid: List[Eid] = field(
        default_factory=list,
        metadata={
            "name": "EID",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
    fid: List[Fid] = field(
        default_factory=list,
        metadata={
            "name": "FID",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        }
    )
