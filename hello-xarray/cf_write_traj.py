#%%
from dataclasses import asdict
from datetime import datetime, timedelta
from os import name
import numpy as np

import xarray as xr
from xarray_dataclasses import asdataarray, asdataset

from cf_classes.attributes import DatasetAttrs

from cf_classes.trajectory import TrajectoryVar, TrajectoryId
from cf_classes.common import WGS1984
#%%
a = asdataset(TrajectoryId('ll'))
a
#%%
a.to_netcdf('test.nc')
#%%
temp_traj = asdataset(
    TrajectoryVar(
        name="sea_water_temperature",
        standard_name="sea_water_temperature",
        long_name="sea_water_temperature",
        units="degree_Celsius",
        data=[[2, 4, 5, 7], [90, 70, 45, 90]],
        time=[
            [
                "1970-01-01T00:00:00.000000000",
                "1970-01-01T10:00:00.000000000",
                "1980-01-01T10:00:00.000000000",
                "1990-01-01T10:00:00.000000000",
            ],
            [
                "1990-01-01T00:00:00.000000000",
                "1990-02-01T10:00:00.000000000",
                "1990-03-01T10:00:00.000000000",
                "1990-04-01T10:00:00.000000000",
            ],
        ],
    )
)

# %%
temp_traj.data.plot(x="time")
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