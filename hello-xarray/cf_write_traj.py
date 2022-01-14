#%%
from dataclasses import asdict
from datetime import datetime, timedelta

import xarray as xr
from xarray_dataclasses import asdataarray

from cf_classes.utils.common import WGS1984
from cf_classes.trajectory import TrajectoryId, TrajectoryAttrs, TrajectoryVariable

#%%
time = [
    "1970-01-01T00:00:00.000000000",
    "1970-01-01T10:00:00.000000000",
    "1980-01-01T10:00:00.000000000",
    "1990-01-01T10:00:00.000000000",
]
longitudes = [10.70, 10.60, 10.50, 10.40]
latitudes = [50.70, 50.60, 50.50, 50.40]
#%%
temperature = TrajectoryVariable(
    name="sea_water_temperature",
    standard_name="sea_water_temperature",
    long_name="sea_water_temperature",
    units="degree_Celsius",
    data=[2, None, 5, 7],
    time=time,
    lat=latitudes,
    lon=longitudes,
    coordinates="time lat lon",
)
# %%
ds = xr.merge([asdataarray(d) for d in [temperature, TrajectoryId("traj1"), WGS1984()]])
# %%
ds.attrs = asdict(
    TrajectoryAttrs(
        title="hei",
        date_created=str(datetime.now()),
        keywords=["hei"],
        trajectory_name="Bergen",
        time_coverage_start=str(ds.time.values[0]),
        time_coverage_end=str(ds.time.values[-1]),
        geospatial_lat_min=float(min(ds.lat)),
        geospatial_lat_max=float(max(ds.lat)),
        geospatial_lon_min=float(min(ds.lon)),
        geospatial_lon_max=float(max(ds.lon)),
    )
)
# %%
ds.to_netcdf("traj.nc")
# %%
