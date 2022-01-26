#%%
from dataclasses import asdict
from datetime import datetime

import xarray as xr
from xarray_dataclasses import asdataarray

from cfxarray.common import wgs1984
from cfxarray.base import dataarraybytime
from cfxarray.trajectory import trajectoryidarray, trajectorycoords, trajectorydataset
from cfxarray.attributes import DatasetAttrs

#%%
time = list(
    map(
        datetime.fromisoformat,
        [
            "1970-01-01T00:00:00",
            "1970-01-01T10:00:00",
            "1980-01-01T10:00:00",
            "1990-01-01T10:00:00",
        ],
    )
)
longitudes = [10.70, 10.60, 10.50, 10.40]
latitudes = [50.70, 50.60, 50.50, 50.40]
#%%
temperature = dataarraybytime(
    name="sea_water_temperature",
    standard_name="sea_water_temperature",
    long_name="sea_water_temperature",
    units="degree_Celsius",
    data=[2, None, 5, 7],
).assign_coords(
    trajectorycoords(
        time=time,
        latitude=latitudes,
        longitude=longitudes,
    )
)
# %%
ds = trajectorydataset("traj1", "title", "summary", ["keyword"], [temperature])
# %%
ds.to_netcdf("traj.nc")
# %%
ds
# %%
