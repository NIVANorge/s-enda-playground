#%%
from datetime import datetime

from cfxarray.base import dataarraybytime, DEFAULT_ENCODING
from cfxarray.trajectory import trajectorycoords, trajectorydataset

#%%
time = list(
    map(
        datetime.fromisoformat,
        [
            "1970-06-01T00:00:00",
            "1970-06-01T10:00:00",
            "1980-06-01T10:00:00",
            "1990-06-01T10:00:00",
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
ds = trajectorydataset([temperature], "sample_trajectory", "title", "summary", ["keyword"])
# %%

ds.to_netcdf("traj2.nc", encoding=DEFAULT_ENCODING)
# %%
ds
# %%
