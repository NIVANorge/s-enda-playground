#%%
from datetime import datetime

import xarray as xr

from cfxarray.profile import depthcoords, profiledataset
from cfxarray.base import dataarraybydepth

# %%
temperature1 = dataarraybydepth(
    name="temperature",
    standard_name="sea_water_temperature",
    long_name="Sea water temperature",
    units="degree_Celsius",
    data=[10, 15],
).assign_coords(
    depthcoords(
        depth=[1, 2],
        time=datetime.fromisoformat("1970-01-01T00:00:00"),
        latitude=59.95,
        longitude=10.75,
    )
)

# %%
ds1 = profiledataset("profile1", "title", "summary", ["keyword"], [temperature1])
# %%
temperature2 = dataarraybydepth(
    name="temperature",
    standard_name="sea_water_temperature",
    long_name="Sea water temperature",
    units="degree_Celsius",
    data=[20, 255, 2000, 100],
).assign_coords(
    depthcoords(
        depth=[1, 2, 10, 20],
        time=datetime.fromisoformat("1980-01-01T00:00:00"),
        latitude=59.95,
        longitude=10.75,
    )
)

# %%
ds2 = profiledataset("profile2", "title", "summary", ["keyword"], [temperature2])
# %%
ds = xr.concat([ds1, ds2], dim="id")
# %%
ds.temperature.sel(id="profile1").plot.line("o")
# %%
