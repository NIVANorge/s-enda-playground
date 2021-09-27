from dataclasses import dataclass, field
from typing import List, Optional
from bindings.gmd.abstract_curve_segment_type import AbstractCurveSegmentType
from bindings.gmd.coordinates import Coordinates
from bindings.gmd.curve_interpolation_type import CurveInterpolationType
from bindings.gmd.point_property import PointProperty
from bindings.gmd.point_rep import PointRep
from bindings.gmd.pos import Pos
from bindings.gmd.pos_list import PosList
from bindings.gmd.vector_type import VectorType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ArcStringByBulgeType(AbstractCurveSegmentType):
    pos: List[Pos] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 2,
            "sequential": True,
        }
    )
    point_property: List[PointProperty] = field(
        default_factory=list,
        metadata={
            "name": "pointProperty",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 2,
            "sequential": True,
        }
    )
    point_rep: List[PointRep] = field(
        default_factory=list,
        metadata={
            "name": "pointRep",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 2,
            "sequential": True,
        }
    )
    pos_list: Optional[PosList] = field(
        default=None,
        metadata={
            "name": "posList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    coordinates: Optional[Coordinates] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    bulge: List[float] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        }
    )
    normal: List[VectorType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        }
    )
    interpolation: CurveInterpolationType = field(
        init=False,
        default=CurveInterpolationType.CIRCULAR_ARC2_POINT_WITH_BULGE,
        metadata={
            "type": "Attribute",
        }
    )
    num_arc: Optional[int] = field(
        default=None,
        metadata={
            "name": "numArc",
            "type": "Attribute",
        }
    )
