#%%
from dataclasses import asdict
from datetime import datetime, timedelta
from os import name
import numpy as np

import xarray as xr
from xarray_dataclasses import asdataarray, asdataset

from cf_classes.attributes import DatasetAttrs
from cf_classes.time_series import (
    Latitude,
    Longitude,
    StationId,
    StationAltitude,
    TimeDataVar
)
from cf_classes.trajectory import TrajDataVar
from cf_classes.common import WGS1984

#%%
temperature = TimeDataVar(
    name='temperature',
    standard_name='sea_water_temperature',
    long_name='Sea water temperature',
    units='degree_Celsius',
    data=[10, 15],
    time=["1970-01-01T00:00:00", "1970-01-01T01:00:10"],
)
#%%
salinity = TimeDataVar(
    name='salinity',
    standard_name='sea_water_salinity',
    long_name='Salinity at some place',
    units='1e-3',
    data=[10, 1500, 15000, 15, 2000, 20000],
    time=np.arange(datetime(1995, 7, 1), datetime(1995, 7, 7), timedelta(days=1)),
)
#%%
conductivity = TimeDataVar(
    name='conductivity',
    standard_name = "sea_water_electrical_conductivity",
    long_name = "Conductivity at depth",
    units = "mS cm-1",
    data=[10, 15, 56],
    time=[
        "1970-01-01T00:00:00",
        "1970-01-01T10:00:00",
        "1980-01-01T10:00:00",
    ],
)
#%%
ds = xr.merge(
    [
        asdataarray(d)
        for d in [
            temperature,
            salinity,
            conductivity,
            WGS1984(),
            Latitude(59.95),
            Longitude(10.75),
            StationAltitude(5),
            StationId("Oslo1")
        ]
    ]
)
#%%
ds.attrs = asdict(
    DatasetAttrs(
        title="hei",
        date_created=str(datetime.now()),
        keywords=["hei"],
        featureType="timeSeries",
    )
)

# %%
ds
# %%
ds = xr.tutorial.load_dataset("air_temperature")

# %%
ds.salinity.plot.line("o")
# %%
ds.to_netcdf("test.nc")
# %%
temp_traj = asdataset(
    TrajDataVar(
        name="sea_water_temperature",
        standard_name="sea_water_temperature",
        long_name="sea_water_temperature",
        units="degree_Celsius",
        data=[[2, 4, 5], [90, 70, 45]],
        trajectory=["first", "second"],
        time=[
            [
                "1970-01-01T00:00:00.000000000",
                "1970-01-01T10:00:00.000000000",
                "1980-01-01T10:00:00.000000000",
            ],
            [
                "1990-01-01T00:00:00.000000000",
                "1990-02-01T10:00:00.000000000",
                "1990-03-01T10:00:00.000000000",
            ],
        ],
    )
)

# %%
temp_traj.data.sel(trajectory="second").plot(x="time").line("o")
# %%
temp_traj.attrs = asdict(
    DatasetAttrs(
        title="hei",
        date_created=str(datetime.now()),
        keywords=["hei"],
        featureType="trajectory",
    )
)

# %%
