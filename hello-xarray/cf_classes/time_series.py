from dataclasses import dataclass, field
from typing import Tuple, Literal

import numpy as np
from xarray_dataclasses import Attr, Coordof, Data, Name

from cf_classes.literals import TIME
from cf_classes.attributes import (
    AltitudeAttrs,
    DatasetAttrs,
    LatitudeAttrs,
    LongitudeAttrs,
)

from cf_classes.common import TimeAxis


@dataclass
class StationId:
    data: Data[None, np.str_]
    name: Name[str] = "station_id"
    long_name: Attr[str] = "Station ID"
    cf_role: Attr[str] = "timeseries_id"


@dataclass
class AltitudeData:
    data: Data[None, np.int16]
    name: Name[str] = "alt"


@dataclass
class StationAltitude(AltitudeAttrs, AltitudeData):
    """Specs for the Z axis."""


@dataclass
class LatitudeData:
    data: Data[None, np.float64]
    name: Name[str] = "lat"


@dataclass
class Latitude(LatitudeAttrs, LatitudeData):
    """Latitude cf data"""


@dataclass
class LongitudeData:
    data: Data[None, np.float64]
    name: Name[str] = "lon"


@dataclass
class Longitude(LongitudeAttrs, LongitudeData):
    pass


@dataclass
class _TimeSeriesAttrs:
    station_name: Attr[str]


@dataclass
class TimeSeriesAttrs(DatasetAttrs, _TimeSeriesAttrs):
    pass
