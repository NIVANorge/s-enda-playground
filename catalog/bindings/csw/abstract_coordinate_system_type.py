from dataclasses import dataclass, field
from typing import List, Optional
from bindings.csw.abstract_coordinate_system_base_type import AbstractCoordinateSystemBaseType
from bindings.csw.cs_id import CsId
from bindings.csw.remarks import Remarks
from bindings.csw.uses_axis import UsesAxis

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractCoordinateSystemType(AbstractCoordinateSystemBaseType):
    """A coordinate system (CS) is the set of coordinate system axes that spans
    a given coordinate space.

    A CS is derived from a set of (mathematical) rules for specifying
    how coordinates in a given space are to be assigned to points. The
    coordinate values in a coordinate tuple shall be recorded in the
    order in which the coordinate system axes associations are recorded,
    whenever those coordinates use a coordinate reference system that
    uses this coordinate system. This abstract complexType shall not be
    used, extended, or restricted, in an Application Schema, to define a
    concrete subtype with a meaning equivalent to a concrete subtype
    specified in this document.

    :ivar cs_id: Set of alternative identifications of this coordinate
        system. The first csID, if any, is normally the primary
        identification code, and any others are aliases.
    :ivar remarks: Comments on or information about this coordinate
        system, including data source information.
    :ivar uses_axis: Ordered sequence of associations to the coordinate
        system axes included in this coordinate system.
    """
    cs_id: List[CsId] = field(
        default_factory=list,
        metadata={
            "name": "csID",
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
    uses_axis: List[UsesAxis] = field(
        default_factory=list,
        metadata={
            "name": "usesAxis",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        }
    )
