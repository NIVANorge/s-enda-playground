from dataclasses import dataclass, field
from typing import Literal, List, Dict, Any

from datetime import datetime

import numpy as np
from xarray_dataclasses import Attr, Coordof, Data, Name
import xarray as xr

from cf_classes.utils.attributes import LatitudeAttrs, LongitudeAttrs, TimeAttrs, VariableAttrs
from attr import asdict, define
from toolz import curry
from cf_classes.dims import TIME, DIMLESS, LONGITUDE, LATITUDE


@define
class TimeSeriesCoord:
    time: xr.Variable
    longitude: xr.Variable
    latitude: xr.Variable


def asstationvariable(station_id: str):
    attrs = {
        "long_name": "Station ID",
        "cf_role": "timeseries_id",
    }
    return xr.DataArray(station_id, name='station_id', dims=DIMLESS, attrs=attrs)


def astimevariable(data, attrs):
    return xr.Variable(TIME, data, attrs)


def astimearray(
    data,
    name: str,
    coords:TimeSeriesCoord,
    attrs: VariableAttrs,
):

    return xr.DataArray(
        data,
        dims=(TIME),
        name=name,
        coords=asdict(coords),
        attrs=asdict(attrs),
    )
