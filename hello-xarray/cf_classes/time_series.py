from dataclasses import dataclass, field
from typing import Literal, List

from datetime import datetime

import numpy as np
from xarray_dataclasses import Attr, Coordof, Data, Name
import xarray as xr

# from cf_classes.utils.literals import TIME
from cf_classes.utils.attributes import DatasetAttrs, TimeAttrs

# from cf_classes.utils.dimless import Latitude, Longitude
# from cf_classes.utils.time import TimeAxis, DataByTime
from attr import define
from toolz import curry


def station_id(station_id: str):
    attrs = {
        "long_name": "Station ID",
        "cf_role": "timeseries_id",
        "encoding": {"dtype": "|S64"},
    }
    return xr.Variable((), station_id, attrs)


def timeseries(data, attrs):
    return xr.Variable("time", data, attrs)
