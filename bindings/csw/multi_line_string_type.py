from dataclasses import dataclass, field
from typing import List
from bindings.csw.abstract_geometric_aggregate_type import AbstractGeometricAggregateType
from bindings.csw.line_string_member import LineStringMember

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MultiLineStringType(AbstractGeometricAggregateType):
    """A MultiLineString is defined by one or more LineStrings, referenced
    through lineStringMember elements.

    Deprecated with GML version 3.0. Use MultiCurveType instead.
    """
    line_string_member: List[LineStringMember] = field(
        default_factory=list,
        metadata={
            "name": "lineStringMember",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
