#%%
from dataclasses import asdict
from datetime import datetime, timedelta

import xarray as xr
from xarray_dataclasses import asdataarray

from cf.time_series import (
    asstationidarray,
    astimearray,
)

# from cf.utils.common import WGS1984
from cf.utils.attributes import DatasetAttrs
from cf.dims import TIME, DIMLESS
from dataclasses import asdict

#%%
# standard names http://vocab.nerc.ac.uk/collection/P07/current/
temperature = astimearray(
    name="temperature",
    data=[10, 15],
    time=[datetime(1999, 10, 4), datetime(1999, 10, 5)],
    longitude=10.75,
    latitude=59.95,
    standard_name="sea_water_temperature",
    long_name="Sea water temperature",
    units="degree_Celsius"
)
#%%
salinity = astimearray(
    name="salinity",
    data=[10, 15],
    time=[datetime(1999, 10, 4), datetime(1999, 10, 5)],
    longitude=10.75,
    latitude=59.95,
    standard_name="sea_water_salinity",
    long_name="Salinity at some place",
    units="1e-3"
)


#%%
conductivity = astimearray(
    name="conductivity",
    data=[10, 15, 100, 40],
    time=[datetime(1999, 10, i) for i in range(1,5)],
    longitude=10.75,
    latitude=59.95,
    standard_name="sea_water_electrical_conductivity",
    long_name="Conductivity at depth",
    units="mS cm-1",
)

#%%
ds = xr.merge(
    [
        temperature,
        salinity,
        conductivity,
        asstationidarray("Oslo1"),
    ]
)
#%%
ds.attrs = asdict(
    DatasetAttrs(
        title="hei",
        date_created=str(datetime.now()),
        keywords=["hei"],
        time_coverage_start=str(ds.time.values[0]),
        time_coverage_end=str(ds.time.values[-1]),
        geospatial_lat_min=float(ds.latitude),
        geospatial_lat_max=float(ds.latitude),
        geospatial_lon_min=float(ds.longitude),
        geospatial_lon_max=float(ds.longitude),
    )
)

# %%
ds.conductivity.plot.line("o")
# %%
ds
# %%
ds.to_netcdf("test.nc", unlimited_dims=["time"])
# %%
