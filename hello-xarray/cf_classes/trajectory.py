from dataclasses import dataclass, field
from typing import Tuple, Literal, Union

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
class TrajectoryId:
    data: Data[None, np.str_]
    cf_role: Attr[str] = "trajectory_id"
    long_name: Attr[str] = "trajectory"

@dataclass
class _TimeSeriesAttrs:
    station_name: Attr[str]


@dataclass
class TimeSeriesAttrs(DatasetAttrs, _TimeSeriesAttrs):
    pass
