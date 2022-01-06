from dataclasses import dataclass, field
from typing import Optional

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
        },
    )
    column_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "columnIndex",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    covariance: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
