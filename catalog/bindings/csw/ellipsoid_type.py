from dataclasses import dataclass, field
from typing import List, Optional
from bindings.csw.ellipsoid_base_type import EllipsoidBaseType
from bindings.csw.ellipsoid_id import EllipsoidId
from bindings.csw.remarks import Remarks
from bindings.csw.second_defining_parameter import SecondDefiningParameter
from bindings.csw.semi_major_axis import SemiMajorAxis

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class EllipsoidType(EllipsoidBaseType):
    """An ellipsoid is a geometric figure that can be used to describe the
    approximate shape of the earth.

    In mathematical terms, it is a surface formed by the rotation of an
    ellipse about its minor axis.

    :ivar ellipsoid_id: Set of alternative identifications of this
        ellipsoid. The first ellipsoidID, if any, is normally the
        primary identification code, and any others are aliases.
    :ivar remarks: Comments on or information about this ellipsoid,
        including source information.
    :ivar semi_major_axis:
    :ivar second_defining_parameter:
    """

    ellipsoid_id: List[EllipsoidId] = field(
        default_factory=list,
        metadata={
            "name": "ellipsoidID",
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
    semi_major_axis: Optional[SemiMajorAxis] = field(
        default=None,
        metadata={
            "name": "semiMajorAxis",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    second_defining_parameter: Optional[SecondDefiningParameter] = field(
        default=None,
        metadata={
            "name": "secondDefiningParameter",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
