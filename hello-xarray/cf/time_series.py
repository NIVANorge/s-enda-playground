from typing import List

from datetime import datetime

import xarray as xr

from cf.utils.attributes import (
    LatitudeAttrs,
    LongitudeAttrs,
    TimeAttrs,
    VariableAttrs,
)
from dataclasses import asdict, dataclass
from toolz import curry
from cf.dims import TIME, DIMLESS, LONGITUDE, LATITUDE


@dataclass
class TimeSeriesCoord:
    time: xr.Variable
    longitude: xr.Variable
    latitude: xr.Variable


def asstationidarray(station_id: str):
    attrs = {
        "long_name": "Station ID",
        "cf_role": "timeseries_id",
    }
    return xr.DataArray(station_id, dims=DIMLESS, name="station_id", attrs=attrs)


def astimearray(
    data,
    name: str,
    standard_name: str,
    long_name: str,
    units: str,
    time: List[datetime],
    longitude: float,
    latitude: float,
):
    return xr.DataArray(
        name=name,
        dims=(TIME),
        data=data,
        coords=asdict(
            TimeSeriesCoord(
                time=xr.Variable(TIME, time, asdict(TimeAttrs())),
                longitude=xr.Variable(DIMLESS, longitude, asdict(LongitudeAttrs())),
                latitude=xr.Variable(DIMLESS, latitude, asdict(LatitudeAttrs())),
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
