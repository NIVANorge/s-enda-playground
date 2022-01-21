from datetime import datetime
import xarray as xr

from cf_classes.utils.attributes import (
    LatitudeAttrs,
    LongitudeAttrs,
    DepthAttrs,
    VariableAttrs,
    DatasetAttrs,
)
from typing import List
from dataclasses import asdict, dataclass
from toolz import compose
from cf_classes.dims import DEPTH, DIMLESS


@dataclass
class DepthCoords:
    depth: xr.Variable
    time: xr.Variable
    longitude: xr.Variable
    latitude: xr.Variable


def asprofileidarray(profile_id: str):
    attrs = {
        "long_name": "Profile ID",
        "cf_role": "profile_id",
    }
    return xr.DataArray(profile_id, dims=DIMLESS, name="profile_id", attrs=attrs)

def asdepthvariable(data, attrs):
    return xr.Variable(DEPTH, data, attrs)


def asprofilearray(
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
    return xr.DataArray(
        name=name,
        dims=(DEPTH),
        data=data,
        coords=asdict(
            DepthCoords(
                depth=xr.Variable(DEPTH, depth, asdict(DepthAttrs())),
                time=xr.Variable(DIMLESS, time, asdict(DepthAttrs())),
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