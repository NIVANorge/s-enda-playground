from typing import List

from datetime import datetime
import xarray as xr

from cfxarray.utils.attributes import (
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


def astrajectoryidarray(trajectory_id: str):
    attrs = {
        "long_name": "trajectory ID",
        "cf_role": "timeseries_id",
    }
    return xr.DataArray(trajectory_id, dims=DIMLESS, name="trajectory_id", attrs=attrs)

@curry
def astimevariable(data, attrs):
    return xr.Variable(TIME, data, attrs)


def astrajectoryarray(
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

#@dataclass
#class TrajectoryVariable(DataByTime):
#    name: Name[str]
#    time: Coordof[TimeAxis] = 0
#    lat: Coordof[LatitudeByTime] = 0
#    lon: Coordof[LongitudeByTime] = 0
#    grid_mapping: Attr[str] = "crs"
#    coordinates: Attr[str] = "time lat lon"
#
    