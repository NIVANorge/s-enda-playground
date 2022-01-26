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


def timeseriesdataset(named_dataarrys: List[xr.DataArray], station_id):
    ds = xr.merge([stationidarray(station_id), wgs1984()] + named_dataarrys)

    ds.attrs = asdict(
        DatasetAttrs(
            title="hei",
            date_created=str(datetime.now()),
            keywords=["hei"],
            time_coverage_start=str(ds.time.min().values),
            time_coverage_end=str(ds.time.max().values),
            geospatial_lat_min=float(ds.latitude.min()),
            geospatial_lat_max=float(ds.latitude.max()),
            geospatial_lon_min=float(ds.longitude.min()),
            geospatial_lon_max=float(ds.longitude.max()),
            featureType="timeSeries",
        )
    )

    return ds
