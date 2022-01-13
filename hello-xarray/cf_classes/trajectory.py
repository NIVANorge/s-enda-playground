from dataclasses import dataclass, field
import imp
from typing import Tuple, Literal, Union

import numpy as np
from xarray_dataclasses import Attr, Coordof, Data, Name

from cf_classes.literals import TIME
from cf_classes.time import DataByTime, TimeAxis, LongitudeByTime, LatitudeByTime
from cf_classes.attributes import (
    DatasetAttrs,
)

@dataclass
class TrajectoryId:
    data: Data[None, Literal['|S64']]
    name: Name[str] = 'trajectory_id'
    cf_role: Attr[str] = "trajectory_id"
    long_name: Attr[str] = "trajectory"


@dataclass
class _TrajectoryAttrs:
    trajectory_name: Attr[str]


@dataclass
class TrajectoryAttrs(DatasetAttrs, _TrajectoryAttrs):
    featureType: Attr[str] = "trajectory"

@dataclass
class TrajectoryVariable(DataByTime):
    name: Name[str]
    time: Coordof[TimeAxis] = 0
    lat: Coordof[LatitudeByTime] = 0
    lon: Coordof[LongitudeByTime] = 0
    grid_mapping: Attr[str] = "crs"
    coordinates: Attr[str] = "time lat lon"
