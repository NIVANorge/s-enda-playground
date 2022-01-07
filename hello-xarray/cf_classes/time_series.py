from dataclasses import dataclass, field
from typing import Tuple, Literal

import numpy as np
from xarray_dataclasses import Attr, Coordof, Data, Name

from cf_classes.literals import DEPTH, TIME, TRAJECTORY, OBS
from cf_classes.attributes import (
    LongitudeAttrs,
    LatitudeAttrs,
    SalinityAttrs,
    ConductivityAttrs,
    WaterTemperatureAttrs,
    TimeAttrs,
    DepthAttrs,
)


@dataclass
class TimeAxis(TimeAttrs):
    """Specs for the Time axis."""

    data: Data[TIME, Literal["datetime64[ns]"]] = field(default_factory=list)
    # units is filled by xarray, based on time interval


@dataclass
class DepthAxis(DepthAttrs):
    """Specs for the Z axis."""
    data: Data[DEPTH, np.int16] = field(default_factory=list)


@dataclass
class Latitude(LatitudeAttrs):
    data: Data[TIME, np.float64] = field(default_factory=list)
    name: Name[str] = "latitude"
    time: Coordof[TimeAxis] = 0


@dataclass
class Longitude(LongitudeAttrs):
    data: Data[TIME, np.float64] = field(default_factory=list)
    name: Name[str] = "longitude"
    time: Coordof[TimeAxis] = 0


@dataclass
class Salinity(SalinityAttrs):
    data: Data[Tuple[TIME, DEPTH], np.float32] = field(default_factory=lambda:[[]])
    name: Name[str] = "salinity"
    time: Coordof[TimeAxis] = 0
    depth: Coordof[DepthAxis] = 1


@dataclass
class Conductivity(ConductivityAttrs):
    data: Data[Tuple[TIME, DEPTH], np.float32] = field(default_factory=lambda:[[]])
    name: Name[str] = "conductivity"
    time: Coordof[TimeAxis] = 0
    depth: Coordof[DepthAxis] = 1


@dataclass
class WaterTemperature(WaterTemperatureAttrs):
    data: Data[Tuple[TIME, DEPTH], np.float32] = field(default_factory=lambda:[[]])
    name: Name[str] = "sea_water_temperature"
    time: Coordof[TimeAxis] = 0
    depth: Coordof[DepthAxis] = 1
