from dataclasses import dataclass, field
from typing import Literal

import numpy as np
from xarray_dataclasses import Attr, Coordof, Data, Name

from cf_classes.literals import TIME
from cf_classes.attributes import DatasetAttrs
from cf_classes.dimless import Latitude, Longitude
from cf_classes.time import TimeAxis, DataByTime


@dataclass
class StationId:
    data: Data[None, Literal["|S64"]]
    name: Name[str] = "station_id"
    long_name: Attr[str] = "Station ID"
    cf_role: Attr[str] = "timeseries_id"


@dataclass
class _TimeSeriesAttrs:
    station_name: Attr[str]


@dataclass
class TimeSeriesAttrs(DatasetAttrs, _TimeSeriesAttrs):
    featureType: Attr[str] = "timeSeries"


@dataclass
class TimeSeriesVariable(DataByTime):
    name: Name[str]
    time: Coordof[TimeAxis] = 0
    lat: Coordof[Latitude] = 0
    lon: Coordof[Longitude] = 0
    grid_mapping: Attr[str] = "crs"
    coordinates: Attr[str] = "time lat lon"
