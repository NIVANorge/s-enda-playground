from dataclasses import dataclass, field
from typing import List, Optional
from generated.gml.pkg_3.pkg_1.pkg_1.base.geometry_basic0d1d import (
    AbstractGeometryType,
    PointPropertyType,
    VectorType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GridEnvelopeType:
    """Provides grid coordinate values for the diametrically opposed corners of
    an envelope that bounds a section of grid.

    The value of a single coordinate is the number of offsets from the
    origin of the grid in the direction of a specific axis.
    """
    low: List[int] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
            "tokens": True,
        }
    )
    high: List[int] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
            "tokens": True,
        }
    )


@dataclass
class GridLimitsType:
    grid_envelope: Optional[GridEnvelopeType] = field(
        default=None,
        metadata={
            "name": "GridEnvelope",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )


@dataclass
class ImplicitGeometry(AbstractGeometryType):
    class Meta:
        name = "_ImplicitGeometry"
        namespace = "http://www.opengis.net/gml"


@dataclass
class GridType(AbstractGeometryType):
    """
    An unrectified grid, which is a network composed of two or more sets of
    equally spaced parallel lines in which the members of each set intersect
    the members of the other sets at right angles.
    """
    limits: Optional[GridLimitsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    axis_name: List[str] = field(
        default_factory=list,
        metadata={
            "name": "axisName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        }
    )
    dimension: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class Grid(GridType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class RectifiedGridType(GridType):
    """
    A rectified grid has an origin and vectors that define its post locations.
    """
    origin: Optional[PointPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    offset_vector: List[VectorType] = field(
        default_factory=list,
        metadata={
            "name": "offsetVector",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        }
    )


@dataclass
class RectifiedGrid(RectifiedGridType):
    """
    Should be substitutionGroup="gml:Grid" but changed in order to accomplish
    Xerces-J schema validation.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml"
