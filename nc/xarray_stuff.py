#%%
from matplotlib import markers
import xarray as xr
from ctd_dataclasses import (
    CTDDatasetAttributes,
    Conductivity,
    Latitude,
    Longitude,
    Salinity,
    WaterTemp,
)
from datetime import datetime
#%%
w_temp = WaterTemp.new(
    [[10, 15], [20, 25]],
    time=["1970-01-01T00:00:00.000000000", "1970-01-01T10:00:00.000000000"],
    depth=[4, 8],
)
#%%
sal = Salinity.new(
    [[10, 150], [15, 20]],
    time=["1970-01-01T00:00:00.000000000", "1970-01-01T10:00:00.000000000"],
    depth=[4, 8],
)
#%%
con = Conductivity.new(
    [[10, 15], [15, 20]],
    time=["1970-01-01T00:00:00.000000000", "1970-01-01T10:00:00.000000000"],
    depth=[4, 8],
)
#%%
ds = xr.merge([w_temp, sal, con])
#%%
ds.attrs = CTDDatasetAttributes("hei", datetime.now(), keywords=["hei"]).__dict__
#%%
ds.sel(depth=8)["sea_water_temperature"].plot.line('o')

# %%
