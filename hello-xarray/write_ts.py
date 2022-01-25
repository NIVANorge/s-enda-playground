#%%
from dataclasses import asdict
from datetime import datetime, timedelta

import xarray as xr
from xarray_dataclasses import asdataarray

from cfxarray.time_series import (
    stationidarray,
)
from cfxarray.common import wgs1984
from cfxarray.attributes import DatasetAttrs
from cfxarray.dims import TIME, DIMLESS
from cfxarray.arrays import dataarraybytime
from cfxarray.time_series import timeseriescoords
from dataclasses import asdict

#%%
# standard names http://vocab.nerc.ac.uk/collection/P07/current/
temperature = dataarraybytime(
    data=[10, 15],
    name="temperature",
    standard_name="sea_water_temperature",
    long_name="Sea water temperature",
    units="degree_Celsius",
).assign_coords(
    timeseriescoords(
        time=[datetime(1999, 10, 4), datetime(1999, 10, 5)],
        latitude=59.95,
        longitude=10.75,
    )
)
#%%
salinity = dataarraybytime(
    data=[10, 15],
    name="salinity",
    standard_name="sea_water_salinity",
    long_name="Salinity at some place",
    units="1e-3",
).assign_coords(
    timeseriescoords(
        time=[datetime(1999, 10, 4), datetime(1999, 10, 5)],
        latitude=59.95,
        longitude=10.75,
    )
)


#%%
conductivity = dataarraybytime(
    data=[10, 15, 100, 40],
    name="conductivity",
    units="mS cm-1",
    standard_name="sea_water_electrical_conductivity",
    long_name="Conductivity at depth",
).assign_coords(
    timeseriescoords(
        time=[datetime(1999, 10, i) for i in range(1, 5)],
        longitude=10.75,
        latitude=59.95,
    )
)

#%%
ds = xr.merge(
    [
        temperature,
        salinity,
        conductivity,
        stationidarray("Oslo1"),
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
        featureType="timeSeries",
    )
)

# %%
ds.conductivity.plot.line("o")
# %%
ds
# %%
ds.to_netcdf("test.nc", unlimited_dims=["time"])
# %%
