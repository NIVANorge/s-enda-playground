from dataclasses import dataclass, field
from typing import Tuple, Literal

import numpy as np
from xarray_dataclasses import Attr, Data, Coordof, Name

from cf_classes.literals import TRAJECTORY, OBS
from cf_classes.attributes import TimeAttrs, DataVarAttrs


@dataclass
class TimeTrajData:
    """Specs for the Time axis."""

    data: Data[Tuple[TRAJECTORY, OBS], Literal["datetime64[ns]"]]


@dataclass
class TimeTraj(TimeAttrs, TimeTrajData):
    """Time Trajectory"""


@dataclass
class Trajectory:
    data: Data[TRAJECTORY, np.str_]
    cf_role: Attr[str] = "trajectory_id"
    long_name: Attr[str] = "trajectory"


@dataclass
class TrajDataVar(DataVarAttrs):
    data: Data[Tuple[TRAJECTORY, OBS], np.float32]
    name: Name[str]
    time: Coordof[TimeTraj] = 0
    trajectory: Coordof[Trajectory] = 0
