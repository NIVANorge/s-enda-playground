#%%
from matplotlib import markers
import xarray as xr
from xarray_dataclasses import asdataarray, asdataset
from cf_dataclasses import (
    CTDDatasetAttributes,
    Conductivity,
    Latitude,
    Longitude,
    Salinity,
    WaterTemperature,
)
from datetime import datetime

#%%
w_temp = WaterTemperature(
    # (4m, 8m)
    [(10, 15), (20, 25)],
    time=["1970-01-01T00:00:00.000000000", "1970-01-01T01:00:00.000000000"],
    depth=[4, 8],
)
#%%
sal = Salinity(
    [(10, 1500, 15000), (15, 2000, 20000)],
    time=["1970-01-01T00:00:00.000000000", "1970-01-01T10:00:00.000000000"],
    depth=[4, 8, 16],
)
#%%
con = Conductivity(
    [(10, 15), (15, 20)],
    time=["1970-01-01T00:00:00.000000000", "1970-01-01T10:00:00.000000000"],
    depth=[4, 8],
)
#%%
ds = xr.merge([asdataarray(d) for d in [w_temp, sal, con]])
#%%
ds.attrs = asdataset(
    CTDDatasetAttributes(
        title="hei", date_created=str(datetime.now()), keywords=["hei"]
    )
).attrs

# %%
ds
# %%
ds.sel(depth=4)
# %%
ds.sel(depth=4).sea_water_temperature.plot.line("o")
# %%
