#%%
from xarray_dataclasses import Attr, Data, Name
from typing import Literal
from dataclasses import dataclass

from xarray_dataclasses import Coordof
import numpy as np

from cf_classes.literals import TIME


from cf_classes.attributes import TimeAttrs, DataVarAttrs


@dataclass
class TimeData:
    data: Data[TIME, Literal["datetime64[ns]"]]
    # units is filled by xarray, based on time interval


@dataclass
class TimeAxis(TimeAttrs, TimeData):
    """Specs for the Time axis."""


@dataclass
class TimeArrayData(DataVarAttrs):
    data: Data[TIME, np.float32]


@dataclass
class TimeArray(TimeArrayData):
    name: Name[str]
    time: Coordof[TimeAxis] = 0
    grid_mapping: Attr[str] = "crs"
    coordinates: Attr[str] = "time lat lon alt"


@dataclass
class WGS1984:
    data: Data[None, np.int8] = 0
    name: Name[str] = "crs"
    grid_mapping_name: Attr[str] = "latitude_longitude"
    longitude_of_prime_meridian: Attr[str] = 0.0
    semi_major_axis: Attr[str] = 6378137.0
    inverse_flattening: Attr[str] = 298.257223563
