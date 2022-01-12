from dataclasses import dataclass, field

import numpy as np
from xarray_dataclasses import Data, Name

from cf_classes.attributes import (
    AltitudeAttrs,
    LatitudeAttrs,
    LongitudeAttrs,
)


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
