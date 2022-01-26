from typing import List

from datetime import datetime

import xarray as xr

from cfxarray.attributes import (
    LatitudeAttrs,
    LongitudeAttrs,
    TimeAttrs,
    DatasetAttrs,
)
from dataclasses import asdict, dataclass
from cfxarray.dims import TIME, DIMLESS, LONGITUDE, LATITUDE
from cfxarray.base import dataarraybytime
from toolz import curry
from cfxarray.common import wgs1984
from cfxarray.base import dataset


@dataclass
class TimeSeriesCoord:
    time: xr.Variable
    longitude: xr.Variable
    latitude: xr.Variable


def stationidarray(station_id: str):
    attrs = {
        "long_name": "Station ID",
        "cf_role": "timeseries_id",
    }
    return xr.DataArray(station_id, dims=DIMLESS, name="station_id", attrs=attrs)


def timeseriescoords(
    time: List[datetime],
    longitude: float,
    latitude: float,
):
    return asdict(
        TimeSeriesCoord(
            time=xr.Variable(TIME, time, asdict(TimeAttrs())),
            longitude=xr.Variable(DIMLESS, longitude, asdict(LongitudeAttrs())),
            latitude=xr.Variable(DIMLESS, latitude, asdict(LatitudeAttrs())),
        )
    )


timeseriesdataset = dataset("timeSeries",  "Station ID", "timeseries_id")


