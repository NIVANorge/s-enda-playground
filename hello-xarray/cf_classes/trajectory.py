
from dataclasses import dataclass, field
from typing import Tuple, Literal

import numpy as np
from xarray_dataclasses import Attr, Data, Coordof, Name

from cf_classes.literals import TRAJECTORY, OBS
from cf_classes.attributes import TimeAttrs, DataVarAttrs


@dataclass
class TrajTimeData:
    """Specs for the Time axis."""

    data: Data[Tuple[TRAJECTORY, OBS], Literal["datetime64[ns]"]]


@dataclass
class TrajectoryTime(TimeAttrs, TrajTimeData):
    """Time Trajectory"""


@dataclass
class TrajectoryId:
    data: Data[None, np.str_]
    cf_role: Attr[str] = "trajectory_id"
    long_name: Attr[str] = "trajectory"


@dataclass
class TrajectoryVar(DataVarAttrs):
    data: Data[Tuple[TRAJECTORY, OBS], np.float32]
    name: Name[str]
    time: Coordof[TrajectoryTime] = 0