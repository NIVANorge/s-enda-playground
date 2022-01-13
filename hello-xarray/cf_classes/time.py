from xarray_dataclasses import Attr, Data, Name
from typing import Literal
from dataclasses import dataclass

from xarray_dataclasses import Coordof
import numpy as np

from cf_classes.literals import TIME

from cf_classes.attributes import (
    TimeAttrs,
    AltitudeAttrs,
    LatitudeAttrs,
    LongitudeAttrs,
)


@dataclass
class TimeData:
    data: Data[TIME, Literal["datetime64[ns]"]]
    # units is filled by xarray, based on time interval


@dataclass
class TimeAxis(TimeAttrs, TimeData):
    """Specs for the Time axis."""


@dataclass
class AltitudeDataByTime:
    data: Data[TIME, np.int16]
    name: Name[str] = "alt"


@dataclass
class AltitudeByTime(AltitudeAttrs, AltitudeDataByTime):
    """Specs for the Z axis."""


@dataclass
class LatitudeDataByTime:
    data: Data[TIME, np.float64]
    name: Name[str] = "lat"


@dataclass
class LatitudeByTime(LatitudeAttrs, LatitudeDataByTime):
    """Latitude cf data"""


@dataclass
class LongitudeDataByTime:
    data: Data[TIME, np.float64]
    name: Name[str] = "lon"


@dataclass
class LongitudeByTime(LongitudeAttrs, LongitudeDataByTime):
    pass
