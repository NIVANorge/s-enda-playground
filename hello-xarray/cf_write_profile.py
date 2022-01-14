#%%
from dataclasses import asdict
from datetime import datetime, timedelta

import xarray as xr
from xarray_dataclasses import asdataarray, asdataset

from cf_classes.common import WGS1984
from cf_classes.profile import ProfileId, ProfileAttrs, DepthProfileVariable

# %%
temperature1 = DepthProfileVariable(
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
ds1 = xr.merge(
    [
        asdataarray(d)
        for d in [temperature1, ProfileId("profile1")]
    ]
)
# %%
temperature2 = DepthProfileVariable(
    name="temperature",
    standard_name="sea_water_temperature",
    long_name="Sea water temperature",
    units="degree_Celsius",
    data=[20, 255, 2000, 100],
    lon=10.75,
    lat=59.95,
    depth=[1, 2, 10, 20],
    time="1980-01-01T00:00:00",
)

# %%
ds2 = xr.merge(
    [
        asdataarray(d)
        for d in [temperature2, ProfileId("profile2")]
    ]
)
# %%
ds = xr.concat([ds1, ds2], dim='profile_id')
#%%
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
ds['crs'] = asdataarray(WGS1984())
# %%
ds.temperature.sel(profile_id=b'profile1').plot.line('o')
# %%
