from dataclasses import asdict, dataclass
from datetime import datetime
from functools import partial
from typing import List

import xarray as xr

from cfxarray.attributes import LatitudeAttrs, LongitudeAttrs, TimeAttrs
from cfxarray.base import dataset
from cfxarray.dims import DIMLESS, TIME


@dataclass
class TimeSeriesCoord:
    time: xr.Variable
    longitude: xr.Variable
    latitude: xr.Variable


def trajectorycoords(
    time: List[datetime],
    longitude: List[float],
    latitude: List[float],
):
    return asdict(
        TimeSeriesCoord(
            time=xr.Variable(TIME, time, asdict(TimeAttrs())),
            longitude=xr.Variable(TIME, longitude, asdict(LongitudeAttrs())),
            latitude=xr.Variable(TIME, latitude, asdict(LatitudeAttrs())),
        )
    )

trajectorydataset =  partial(dataset, "trajectory")
 