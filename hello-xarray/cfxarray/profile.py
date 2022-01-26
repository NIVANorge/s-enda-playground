from datetime import datetime
import xarray as xr

from cfxarray.attributes import (
    LatitudeAttrs,
    LongitudeAttrs,
    DepthAttrs,
    VariableAttrs,
    TimeAttrs,
)
from typing import List
from dataclasses import asdict, dataclass
from toolz import compose
from cfxarray.dims import DEPTH, DIMLESS
from cfxarray.base import dataset


@dataclass
class DepthCoords:
    depth: xr.Variable
    time: xr.Variable
    longitude: xr.Variable
    latitude: xr.Variable


def profileidarray(profile_id: str):
    attrs = {
        "long_name": "Profile ID",
        "cf_role": "profile_id",
    }
    return xr.DataArray(profile_id, dims=DIMLESS, name="profile_id", attrs=attrs)


def depthcoords(
    depth: List[float],
    time: datetime,
    longitude: float,
    latitude: float,
):
    return asdict(
        DepthCoords(
            depth=xr.Variable(DEPTH, depth, asdict(DepthAttrs())),
            time=xr.Variable(DIMLESS, time, asdict(TimeAttrs())),
            longitude=xr.Variable(DIMLESS, longitude, asdict(LongitudeAttrs())),
            latitude=xr.Variable(DIMLESS, latitude, asdict(LatitudeAttrs())),
        )
    )

profiledataset = dataset("profile",  "profile ID", "profile_id")
