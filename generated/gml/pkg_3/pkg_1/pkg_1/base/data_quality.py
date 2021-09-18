from dataclasses import dataclass, field
from typing import List, Optional
from generated.gml.pkg_3.pkg_1.pkg_1.base.basic_types import (
    CodeType,
    MeasureType,
)
from generated.gml.pkg_3.pkg_1.pkg_1.base.units import UnitOfMeasure

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CovarianceElementType:
    """
    An element of a covariance matrix.
    """
    row_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "rowIndex",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    column_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "columnIndex",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    covariance: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )


@dataclass
class ColumnIndex:
    """
    Column number of this covariance element value.
    """
    class Meta:
        name = "columnIndex"
        namespace = "http://www.opengis.net/gml"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Covariance:
    """
    Value of covariance matrix element.
    """
    class Meta:
        name = "covariance"
        namespace = "http://www.opengis.net/gml"

    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class RowIndex:
    """
    Row number of this covariance element value.
    """
    class Meta:
        name = "rowIndex"
        namespace = "http://www.opengis.net/gml"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class IncludesElement(CovarianceElementType):
    class Meta:
        name = "includesElement"
        namespace = "http://www.opengis.net/gml"


@dataclass
class MeasureDescription(CodeType):
    """
    A description of the position accuracy parameter(s) provided.
    """
    class Meta:
        name = "measureDescription"
        namespace = "http://www.opengis.net/gml"


@dataclass
class Result(MeasureType):
    """
    A quantitative result defined by the evaluation procedure used, and
    identified by the measureDescription.
    """
    class Meta:
        name = "result"
        namespace = "http://www.opengis.net/gml"


@dataclass
class AbstractPositionalAccuracyType:
    """
    Position error estimate (or accuracy) data.
    """
    measure_description: Optional[MeasureDescription] = field(
        default=None,
        metadata={
            "name": "measureDescription",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class AbsoluteExternalPositionalAccuracyType(AbstractPositionalAccuracyType):
    """
    Closeness of reported coordinate values to values accepted as or being
    true.
    """
    result: Optional[Result] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )


@dataclass
class CovarianceMatrixType(AbstractPositionalAccuracyType):
    """
    Error estimate covariance matrix.

    :ivar unit_of_measure: Ordered sequence of units of measure,
        corresponding to the row and column index numbers of the
        covariance matrix, starting with row and column 1 and ending
        with row/column N. Each unit of measure is for the ordinate
        reflected in the relevant row and column of the covariance
        matrix.
    :ivar includes_element: Unordered set of elements in this covariance
        matrix. Because the covariance matrix is symmetrical, only the
        elements in the upper or lower diagonal part (including the main
        diagonal) of the matrix need to be specified. Any zero valued
        covariance elements can be omitted.
    """
    unit_of_measure: List[UnitOfMeasure] = field(
        default_factory=list,
        metadata={
            "name": "unitOfMeasure",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        }
    )
    includes_element: List[IncludesElement] = field(
        default_factory=list,
        metadata={
            "name": "includesElement",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        }
    )


@dataclass
class RelativeInternalPositionalAccuracyType(AbstractPositionalAccuracyType):
    """
    Closeness of the relative positions of two or more positions to their
    respective relative positions accepted as or being true.
    """
    result: Optional[Result] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )


@dataclass
class PositionalAccuracy(AbstractPositionalAccuracyType):
    class Meta:
        name = "_positionalAccuracy"
        namespace = "http://www.opengis.net/gml"


@dataclass
class AbsoluteExternalPositionalAccuracy(AbsoluteExternalPositionalAccuracyType):
    class Meta:
        name = "absoluteExternalPositionalAccuracy"
        namespace = "http://www.opengis.net/gml"


@dataclass
class CovarianceMatrix(CovarianceMatrixType):
    class Meta:
        name = "covarianceMatrix"
        namespace = "http://www.opengis.net/gml"


@dataclass
class RelativeInternalPositionalAccuracy(RelativeInternalPositionalAccuracyType):
    class Meta:
        name = "relativeInternalPositionalAccuracy"
        namespace = "http://www.opengis.net/gml"
