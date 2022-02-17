from dataclasses import dataclass, field
from typing import Optional
from bindings.gmd.abstract_gmltype import AbstractGmltype
from bindings.gmd.data_source import DataSource
from bindings.gmd.valid_time import ValidTime

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractTimeSliceType(AbstractGmltype):
    valid_time: Optional[ValidTime] = field(
        default=None,
        metadata={
            "name": "validTime",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    data_source: Optional[DataSource] = field(
        default=None,
        metadata={
            "name": "dataSource",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
