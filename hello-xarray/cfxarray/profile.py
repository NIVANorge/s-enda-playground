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


def profilearray(
    data,
    name: str,
    standard_name: str,
    long_name: str,
    units: str,
):
    return xr.DataArray(
        name=name,
        dims=(DEPTH),
        data=data,
        attrs=asdict(
            VariableAttrs(
                standard_name=standard_name,
                long_name=long_name,
                units=units,
            )
        ),
    )


def profilearraycoords(
    data,
    name: str,
    standard_name: str,
    long_name: str,
    units: str,
    depth: List[float],
    time: datetime,
    longitude: float,
    latitude: float,
):
    return profilearray(data, name, standard_name, long_name, units).assign_coords(
        asdict(
            DepthCoords(
                depth=xr.Variable(DEPTH, depth, asdict(DepthAttrs())),
                time=xr.Variable(DIMLESS, time, asdict(TimeAttrs())),
                longitude=xr.Variable(DIMLESS, longitude, asdict(LongitudeAttrs())),
                latitude=xr.Variable(DIMLESS, latitude, asdict(LatitudeAttrs())),
            )
        ))
    