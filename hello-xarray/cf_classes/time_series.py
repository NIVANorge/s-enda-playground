from dataclasses import dataclass, field
from typing import Tuple, Literal

import numpy as np
from xarray_dataclasses import Attr, Coordof, Data, Name

from cf_classes.literals import TIME, STATION
from cf_classes.attributes import (
    AltitudeAttrs,
    DatasetAttrs,
    LatitudeAttrs,
    TimeAttrs,
    LongitudeAttrs,
    DataVarAttrs
)


@dataclass
class StationId:
    data: Data[None, np.str_]
    name: Name[str] = 'station_id'
    long_name: Attr[str] = "Station ID"
    cf_role: Attr[str] = "timeseries_id"



@dataclass
class TimeData:
    data: Data[TIME, Literal["datetime64[ns]"]]
    # units is filled by xarray, based on time interval


@dataclass
class TimeAxis(TimeAttrs, TimeData):
    """Specs for the Time axis."""


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
class TimeSeriesVar(DataVarAttrs):
    data: Data[TIME, np.float32]
    name: Name[str]
    time: Coordof[TimeAxis] = 0
    grid_mapping: Attr[str] = "crs"
    coordinates: Attr[str] = "time lat lon alt"

@dataclass
class _TimeSeriesAttrs:
    station_name: Attr[str]

@dataclass
class TimeSeriesAttrs(DatasetAttrs, _TimeSeriesAttrs):
    pass
