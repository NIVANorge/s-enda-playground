from dataclasses import dataclass, field
from typing import Literal

import numpy as np
from xarray_dataclasses import Data, Name

from cf_classes.attributes import (AltitudeAttrs, LatitudeAttrs,
                                   LongitudeAttrs, TimeAttrs)


@dataclass
class AltitudeData:
    data: Data[None, np.int16]
    name: Name[str] = "alt"


@dataclass
class Altitude(AltitudeAttrs, AltitudeData):
    """Specs for the Z axis."""


@dataclass
class LatitudeData:
    data: Data[None, np.float64]
    name: Name[str] = "lat"


@dataclass
class Latitude(LatitudeAttrs, LatitudeData):
    """Latitude cf data"""


@dataclass
class LongitudeData:
    data: Data[None, np.float64]
    name: Name[str] = "lon"


@dataclass
class Longitude(LongitudeAttrs, LongitudeData):
    pass


@dataclass
class TimeData:
    data: Data[None, Literal["datetime64[ns]"]]
    name: Name[str] = "time"


@dataclass
class Time(TimeAttrs, TimeData):
    pass
