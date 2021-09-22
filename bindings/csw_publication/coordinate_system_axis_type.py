from dataclasses import dataclass, field
from typing import List, Optional
from bindings.csw_publication.axis_abbrev import AxisAbbrev
from bindings.csw_publication.axis_direction import AxisDirection
from bindings.csw_publication.axis_id import AxisId
from bindings.csw_publication.coordinate_system_axis_base_type import CoordinateSystemAxisBaseType
from bindings.csw_publication.remarks import Remarks

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CoordinateSystemAxisType(CoordinateSystemAxisBaseType):
    """
    Definition of a coordinate system axis.

    :ivar axis_id: Set of alternative identifications of this coordinate
        system axis. The first axisID, if any, is normally the primary
        identification code, and any others are aliases.
    :ivar remarks: Comments on or information about this coordinate
        system axis, including data source information.
    :ivar axis_abbrev:
    :ivar axis_direction:
    :ivar uom:
    """
    axis_id: List[AxisId] = field(
        default_factory=list,
        metadata={
            "name": "axisID",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    remarks: Optional[Remarks] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    axis_abbrev: Optional[AxisAbbrev] = field(
        default=None,
        metadata={
            "name": "axisAbbrev",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    axis_direction: Optional[AxisDirection] = field(
        default=None,
        metadata={
            "name": "axisDirection",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    uom: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
