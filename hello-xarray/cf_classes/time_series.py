from dataclasses import dataclass, field
from typing import Tuple, Literal

import numpy as np
from xarray_dataclasses import Attr, Coordof, Data, Name

from cf_classes.literals import TIME, STATION
from cf_classes.attributes import (
    AltitudeAttrs,
    LatitudeAttrs,
    TimeAttrs,
    LongitudeAttrs,
    DataVarAttrs
)


@dataclass
class StationId:
    data: Data[Literal[()], np.str_]
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
    data: Data[Literal[()], np.int16]
    name: Name[str] = "alt"


@dataclass
class StationAltitude(AltitudeAttrs, AltitudeData):
    """Specs for the Z axis."""


@dataclass
class LatitudeData:
    data: Data[Literal[()], np.float64]
    name: Name[str] = "lat"


@dataclass
class Latitude(LatitudeAttrs, LatitudeData):
    """Latitude cf data"""


@dataclass
class LongitudeData:
    data: Data[Literal[()], np.float64]
    name: Name[str] = "lon"


@dataclass
class Longitude(LongitudeAttrs, LongitudeData):
    pass


@dataclass
class TimeDataVar(DataVarAttrs):
    data: Data[TIME, np.float32]
    name: Name[str]
    time: Coordof[TimeAxis] = 0
    grid_mapping: Attr[str] = "crs"
    coordinates: Attr[str] = "time lat lon alt"
