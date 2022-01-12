from dataclasses import dataclass, field

import numpy as np
from xarray_dataclasses import Attr, Coordof, Data, Name

from cf_classes.literals import TIME
from cf_classes.attributes import DatasetAttrs


@dataclass
class StationId:
    data: Data[None, np.str_]
    name: Name[str] = "station_id"
    long_name: Attr[str] = "Station ID"
    cf_role: Attr[str] = "timeseries_id"


@dataclass
class _TimeSeriesAttrs:
    station_name: Attr[str]


@dataclass
class TimeSeriesAttrs(DatasetAttrs, _TimeSeriesAttrs):
    featureType: Attr[str] = "timeSeries"
