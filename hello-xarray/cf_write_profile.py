#%%
from dataclasses import asdict
from datetime import datetime, timedelta

import xarray as xr
from xarray_dataclasses import asdataarray, asdataset

from cf_classes.common import WGS1984
from cf_classes.profile import ProfileId, ProfileAttrs, DepthProfileVariable

# %%
temperature = DepthProfileVariable(
    name="temperature",
    standard_name="sea_water_temperature",
    long_name="Sea water temperature",
    units="degree_Celsius",
    data=[10, 15],
    lon=10.75,
    lat=59.95,
    depth=[1, 2],
    time="1970-01-01T00:00:00",
)

# %%
# %%
ds = xr.merge(
    [
        asdataarray(d)
        for d in [temperature, ProfileId("profile1"), WGS1984()]
    ]
)
# %%
ds.attrs = asdict(
    ProfileAttrs(
        title="hei",
        date_created=str(datetime.now()),
        keywords=["hei"],
        profile_name="Oslo",
        time_coverage_start=str(ds.time),
        time_coverage_end=str(ds.time),
        geospatial_lat_min=float(ds.lat),
        geospatial_lat_max=float(ds.lat),
        geospatial_lon_min=float(ds.lon),
        geospatial_lon_max=float(ds.lon),
    )
)
# %%
ds
# %%
