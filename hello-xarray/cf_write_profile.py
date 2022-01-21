#%%
from dataclasses import asdict
from datetime import datetime, timedelta

import xarray as xr
from xarray_dataclasses import asdataarray, asdataset

from cf_classes.utils.common import WGS1984
from cf_classes.profile import asprofilearray, asprofileidarray, ProfileAttrs
from cf_classes.utils.attributes import DatasetAttrs
from toolz.dicttoolz import merge

# %%
temperature1 = asprofilearray(
    name="temperature",
    standard_name="sea_water_temperature",
    long_name="Sea water temperature",
    units="degree_Celsius",
    data=[10, 15],
    longitude=10.75,
    latitude=59.95,
    depth=[1, 2],
    time=datetime.fromisoformat("1970-01-01T00:00:00"),
)

# %%
ds1 = xr.merge([temperature1, asprofileidarray("profile1")])
# %%
temperature2 = asprofilearray(
    name="temperature",
    standard_name="sea_water_temperature",
    long_name="Sea water temperature",
    units="degree_Celsius",
    data=[20, 255, 2000, 100],
    longitude=10.75,
    latitude=59.95,
    depth=[1, 2, 10, 20],
    time=datetime.fromisoformat("1980-01-01T00:00:00"),
)

# %%
ds2 = xr.merge([temperature2, asprofileidarray("profile2")])
# %%
ds = xr.concat([ds1, ds2], dim="profile_id")
#%%
ds.attrs = asdict(
        DatasetAttrs(
            title="hei",
            date_created=str(datetime.now()),
            keywords=["hei"],
            profile_name="oslo",
            time_coverage_start=str(ds.time.min().values),
            time_coverage_end=str(ds.time.max().values),
            geospatial_lat_min=float(ds.latitude.min().values),
            geospatial_lat_max=float(ds.latitude.max().values),
            geospatial_lon_min=float(ds.longitude.min().values),
            geospatial_lon_max=float(ds.longitude.max().values),
        ))

# %%
ds["crs"] = asdataarray(WGS1984())
# %%
ds.temperature.sel(profile_id="profile1").plot.line("o")
# %%