from dataclasses import dataclass, field
from typing import Tuple, Literal

import numpy as np
from xarray_dataclasses import Attr, Coordof, Data, Name

from cf_classes.literals import DEPTH, TIME, TRAJECTORY, OBS



@dataclass
class TimeAxis:
    """Specs for the Time axis."""
    data: Data[TIME, Literal["datetime64[ns]"]]
    # units is filled by xarray, based on time interval


@dataclass
class DepthAxis:
    """Specs for the Z axis."""
    data: Data[DEPTH, np.int16]


@dataclass
class Latitude:
    data: Data[TIME, np.float64]
    name: Name[str] = "latitude"
    time: Coordof[TimeAxis] = 0


@dataclass
class Longitude:
    data: Data[TIME, np.float64]
    name: Name[str] = "longitude"
    time: Coordof[TimeAxis] = 0


@dataclass
class Salinity:
    data: Data[Tuple[TIME, DEPTH], np.float32]
    name: Name[str] = "salinity"
    time: Coordof[TimeAxis] = 0
    depth: Coordof[DepthAxis] = 0


@dataclass
class Conductivity:
    data: Data[Tuple[TIME, DEPTH], np.float32]
    name: Name[str] = "conductivity"
    time: Coordof[TimeAxis] = 0
    depth: Coordof[DepthAxis] = 0


@dataclass
class WaterTemperature:
    data: Data[Tuple[TIME, DEPTH], np.float32]
    name: Name[str] = "sea_water_temperature"
    time: Coordof[TimeAxis] = 0
    depth: Coordof[DepthAxis] = 0
