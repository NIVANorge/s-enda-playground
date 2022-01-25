from typing import List

from datetime import datetime
import xarray as xr

from cfxarray.attributes import (
    LatitudeAttrs,
    LongitudeAttrs,
    TimeAttrs,
    VariableAttrs,
)
from dataclasses import asdict, dataclass
from toolz import curry
from cfxarray.dims import TIME, DIMLESS
from cfxarray.arrays import dataarraybytime


@dataclass
class TimeSeriesCoord:
    time: xr.Variable
    longitude: xr.Variable
    latitude: xr.Variable


def trajectoryidarray(trajectory_id: str):
    attrs = {
        "long_name": "trajectory ID",
        "cf_role": "timeseries_id",
    }
    return xr.DataArray(trajectory_id, dims=DIMLESS, name="trajectory_id", attrs=attrs)


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
