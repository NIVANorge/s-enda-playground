from dataclasses import dataclass, field
from typing import List, Optional
from bindings.csw.greenwich_longitude import GreenwichLongitude
from bindings.csw.meridian_id import MeridianId
from bindings.csw.prime_meridian_base_type import PrimeMeridianBaseType
from bindings.csw.remarks import Remarks

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class PrimeMeridianType(PrimeMeridianBaseType):
    """
    A prime meridian defines the origin from which longitude values are
    determined.

    :ivar meridian_id: Set of alternative identifications of this prime
        meridian. The first meridianID, if any, is normally the primary
        identification code, and any others are aliases.
    :ivar remarks: Comments on or information about this prime meridian,
        including source information.
    :ivar greenwich_longitude:
    """

    meridian_id: List[MeridianId] = field(
        default_factory=list,
        metadata={
            "name": "meridianID",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    remarks: Optional[Remarks] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    greenwich_longitude: Optional[GreenwichLongitude] = field(
        default=None,
        metadata={
            "name": "greenwichLongitude",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
