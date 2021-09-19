from dataclasses import dataclass, field
from typing import Optional
from bindings.csw.abstract_gmltype import AbstractGmltype
from bindings.csw.data_source import DataSource
from bindings.csw.valid_time import ValidTime

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractTimeSliceType(AbstractGmltype):
    """A timeslice encapsulates the time-varying properties of a dynamic
    feature--it must be extended to represent a timestamped projection of a
    feature.

    The dataSource property describes how the temporal data was
    acquired.
    """
    valid_time: Optional[ValidTime] = field(
        default=None,
        metadata={
            "name": "validTime",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    data_source: Optional[DataSource] = field(
        default=None,
        metadata={
            "name": "dataSource",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
