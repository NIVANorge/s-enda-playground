#%%
from datetime import datetime

from cfxarray.base import dataarraybytime
from cfxarray.trajectory import trajectorycoords, trajectorydataset

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
ds = trajectorydataset([temperature], "traj1", "title", "summary", ["keyword"])
# %%
ds.time.encoding['units'] = 'seconds since 1970-01-01 00:00:00'

ds.to_netcdf("traj.nc")
# %%
ds
# %%
