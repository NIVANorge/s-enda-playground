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


def trajectoryarray(
    data,
    name: str,
    standard_name: str,
    long_name: str,
    units: str,
    time: List[datetime],
    longitude: List[float],
    latitude: List[float],
):
    return xr.DataArray(
        name=name,
        dims=(TIME),
        data=data,
        coords=asdict(
            TimeSeriesCoord(
                time=xr.Variable(TIME, time, asdict(TimeAttrs())),
                longitude=xr.Variable(TIME, longitude, asdict(LongitudeAttrs())),
                latitude=xr.Variable(TIME, latitude, asdict(LatitudeAttrs())),
            )
        ),
        attrs=asdict(
            VariableAttrs(
                standard_name=standard_name,
                long_name=long_name,
                units=units,
            )
        ),
    )


def trajectoryarraycoords(
    data,
    name: str,
    standard_name: str,
    long_name: str,
    units: str,
    time: List[datetime],
    longitude: List[float],
    latitude: List[float],
):
    return trajectoryarray(data, name, standard_name, long_name, units).assign_coords(
        asdict(
            TimeSeriesCoord(
                time=xr.Variable(TIME, time, asdict(TimeAttrs())),
                longitude=xr.Variable(TIME, longitude, asdict(LongitudeAttrs())),
                latitude=xr.Variable(TIME, latitude, asdict(LatitudeAttrs())),
            )
        )
    )