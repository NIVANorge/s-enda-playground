from typing import List, Tuple, Union, Any

import xarray as xr
from datetime import datetime

from cfxarray.attributes import (
    VariableAttrs,
)
from dataclasses import asdict
from toolz import curry
from cfxarray.dims import TIME, DEPTH, DIMLESS
from cfxarray.attributes import DatasetAttrs
from cfxarray.common import wgs1984


@curry
def dataarray(
    dims: Union[Tuple, str],
    data: List[Any],
    name: str,
    standard_name: str,
    long_name: str,
    units: str,
) -> xr.DataArray:
    return xr.DataArray(
        name=name,
        dims=dims,
        data=data,
        attrs=asdict(
            VariableAttrs(
                standard_name=standard_name,
                long_name=long_name,
                units=units,
            )
        ),
    )


dataarraybytime = dataarray(TIME)

dataarraybydepth = dataarray(DEPTH)

def idarray(id: str, long_name: str, cf_role:str):
    attrs = {
        "long_name": long_name,
        "cf_role": cf_role,
    }
    return xr.DataArray(id, dims=DIMLESS, name="id", attrs=attrs)


@curry
def dataset(
    feature_type: str,
    id_long_name,
    cf_role,
    named_dataarrays,
    id: str,
    title: str,
    summary: str,
    keywords: List[str],
):
    ds = xr.merge(named_dataarrays + [idarray(id, id_long_name, cf_role), wgs1984()])

    ds.attrs = asdict(
        DatasetAttrs(
            title=title,
            summary=summary,
            date_created=str(datetime.now()),
            keywords=keywords,
            time_coverage_start=str(ds.time.min().values),
            time_coverage_end=str(ds.time.max().values),
            geospatial_lat_min=float(ds.latitude.min()),
            geospatial_lat_max=float(ds.latitude.max()),
            geospatial_lon_min=float(ds.longitude.min()),
            geospatial_lon_max=float(ds.longitude.max()),
            featureType=feature_type,
        )
    )
    return ds