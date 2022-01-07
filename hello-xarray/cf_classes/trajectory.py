from dataclasses import dataclass, field
from typing import Tuple, Literal

import numpy as np
from xarray_dataclasses import Attr, Data, Coordof, Name

from cf_classes.literals import TRAJECTORY, OBS
from cf_classes.attributes import TimeAttrs, WaterTemperatureAttrs

@dataclass
class Time(TimeAttrs):
    """Specs for the Time axis."""
    data: Data[Tuple[TRAJECTORY, OBS], Literal["datetime64[ns]"]] = field(default_factory=list)

@dataclass
class Trajectory:
    data: Data[TRAJECTORY, np.str_] = field(default_factory=list)
    cf_role: Attr[str] = "trajectory_id"
    long_name: Attr[str] = "trajectory"

@dataclass
class WaterTemperature(WaterTemperatureAttrs):
    data: Data[Tuple[TRAJECTORY, OBS], np.float32] = field(default_factory=list)
    name: Name[str] = "sea_water_temperature"
    time: Coordof[Time] = 0
    trajectory: Coordof[Trajectory] = 0