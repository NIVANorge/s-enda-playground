from dataclasses import dataclass, field
from typing import Tuple, Literal

import numpy as np
from xarray_dataclasses import Attr, Coordof, Data, Name

from cf_classes.literals import DEPTH, TIME, TRAJECTORY, OBS
from cf_classes.attributes import (
    DepthAttrs,
    LatitudeAttrs,
    TimeAttrs,
    LongitudeAttrs,
    SalinityAttrs,
    ConductivityAttrs,
    WaterTemperatureAttrs,
)


@dataclass
class TimeData:
    data: Data[TIME, Literal["datetime64[ns]"]]
    # units is filled by xarray, based on time interval


@dataclass
class TimeAxis(TimeAttrs, TimeData):
    """Specs for the Time axis."""


@dataclass
class DepthData:
    data: Data[DEPTH, np.int16]


@dataclass
class DepthAxis(DepthAttrs, DepthData):
    """Specs for the Z axis."""


@dataclass
class LatitudeData:
    data: Data[TIME, np.float64]
    name: Name[str] = "latitude"
    time: Coordof[TimeAxis] = 0


@dataclass
class Latitude(LatitudeAttrs, LatitudeData):
    """Latitude cf data"""


@dataclass
class LongitudeData:
    data: Data[TIME, np.float64]
    name: Name[str] = "longitude"
    time: Coordof[TimeAxis] = 0


@dataclass
class Longitude(LongitudeAttrs, LongitudeData):
    pass


@dataclass
class SalinityData:
    data: Data[Tuple[TIME, DEPTH], np.float32]
    name: Name[str] = "salinity"
    time: Coordof[TimeAxis] = 0
    depth: Coordof[DepthAxis] = 0


@dataclass
class Salinity(SalinityAttrs, SalinityData):
    pass


@dataclass
class ConductivityData:
    data: Data[Tuple[TIME, DEPTH], np.float32]
    name: Name[str] = "conductivity"
    time: Coordof[TimeAxis] = 0
    depth: Coordof[DepthAxis] = 0


@dataclass
class Conductivity(ConductivityAttrs, ConductivityData):
    pass


@dataclass
class WaterTemperatureData:
    data: Data[Tuple[TIME, DEPTH], np.float32]
    name: Name[str] = "sea_water_temperature"
    time: Coordof[TimeAxis] = 0
    depth: Coordof[DepthAxis] = 0


@dataclass
class WaterTemperature(WaterTemperatureAttrs, WaterTemperatureData):
    pass
