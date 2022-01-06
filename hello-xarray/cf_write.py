#%%
from dataclasses import asdict
from datetime import datetime

import xarray as xr
from xarray_dataclasses import asdataarray, asdataset

from cf_classes.attributes import DatasetAttributes
from cf_classes.dataarrays import (
    Conductivity,
    Latitude,
    Longitude,
    Salinity,
    WaterTemperature,
)

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
    [(10, 15), (15, 20), (1.5, 2.0)],
    time=[
        "1970-01-01T00:00:00.000000000",
        "1970-01-01T10:00:00.000000000",
        "1980-01-01T10:00:00.000000000",
    ],
    depth=[4, 8],
)
#%%
ds = xr.merge([asdataarray(d) for d in [w_temp, sal, con]])
#%%
ds.attrs = asdict(
    DatasetAttributes(
        title="hei", date_created=str(datetime.now()), keywords=["hei"], featureType="traectory"
    )
)

# %%
ds
# %%
ds.sel(depth=4)
# %%
ds.sel(depth=4).sea_water_temperature.plot.line("o")
# %%
ds.to_netcdf("test.nc")
# %%
