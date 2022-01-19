from dataclasses import dataclass, field
from typing import Literal, List, Dict, Any

from datetime import datetime

import numpy as np
from xarray_dataclasses import Attr, Coordof, Data, Name
import xarray as xr

from cf_classes.utils.attributes import DatasetAttrs, TimeAttrs

from attr import define
from toolz import curry


def asstationvariable(station_id: str):
    attrs = {
        "long_name": "Station ID",
        "cf_role": "timeseries_id",
    }
    return xr.Variable((), station_id, attrs)


def astimevariable(data, attrs):
    return xr.Variable("time", data, attrs)


def astimearray(
    data, time: List[datetime], lon: float, lat: float, attrs: Dict[str, Any]
):
    pass
