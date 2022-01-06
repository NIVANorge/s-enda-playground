from dataclasses import dataclass
from typing import Tuple

import numpy as np
from xarray_dataclasses import Attr, Coordof, Data, Name

from cf_classes.axes import DepthAxis, TimeAxis
from cf_classes.literals import DEPTH, TIME


@dataclass
class Latitude:
    data: Data[TIME, np.float64]
    name: Name[str] = "latitude"
    time: Coordof[TimeAxis] = 0
    standard_name: Attr[str] = "latitude"
    units: Attr[str] = "degree_north"
    valid_min: Attr[float] = -90.0
    valid_max: Attr[float] = 90.0


@dataclass
class Longitude:
    data: Data[TIME, np.float64]
    name: Name[str] = "longitude"
    time: Coordof[TimeAxis] = 0
    standard_name: Attr[str] = "longitude"
    units: Attr[str] = "degree_east"
    valid_min: Attr[float] = -180.0
    valid_max: Attr[float] = 180.0


@dataclass
class Salinity:
    data: Data[Tuple[TIME, DEPTH], np.float32]
    name: Name[str] = "salinity"
    time: Coordof[TimeAxis] = 0
    depth: Coordof[DepthAxis] = 0
    standard_name: Attr[str] = "sea_water_salinity"
    long_name: Attr[str] = "Salinity at depth"
    units: Attr[str] = "1e-3"
    valid_min: Attr[float] = 10.0
    valid_max: Attr[float] = 40.0


@dataclass
class Conductivity:
    data: Data[Tuple[TIME, DEPTH], np.float32]
    name: Name[str] = "conductivity"
    time: Coordof[TimeAxis] = 0
    depth: Coordof[DepthAxis] = 0
    standard_name: Attr[str] = "sea_water_electrical_conductivity"
    long_name: Attr[str] = "Conductivity at depth"
    units: Attr[str] = "mS cm-1"
    valid_min: Attr[float] = 10.0
    valid_max: Attr[float] = 50.0


@dataclass
class WaterTemperature:
    data: Data[Tuple[TIME, DEPTH], np.float32]
    name: Name[str] = "sea_water_temperature"
    time: Coordof[TimeAxis] = 0
    depth: Coordof[DepthAxis] = 0
    standard_name: Attr[str] = "sea_water_temperature"
    long_name: Attr[str] = "Water Temperature at depth"
    units: Attr[str] = "degree_Celsius"
    valid_min: Attr[float] = 0.0
    valid_max: Attr[float] = 25.0
