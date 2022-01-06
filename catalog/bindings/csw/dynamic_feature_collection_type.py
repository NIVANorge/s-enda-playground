from dataclasses import dataclass, field
from typing import Optional
from bindings.csw.data_source import DataSource
from bindings.csw.feature_array_property_type import FeatureCollectionType
from bindings.csw.history import History
from bindings.csw.track import Track
from bindings.csw.valid_time import ValidTime

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DynamicFeatureCollectionType(FeatureCollectionType):
    """
    A dynamic feature collection may possess a history and/or a timestamp.
    """

    valid_time: Optional[ValidTime] = field(
        default=None,
        metadata={
            "name": "validTime",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    track: Optional[Track] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    history: Optional[History] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
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
