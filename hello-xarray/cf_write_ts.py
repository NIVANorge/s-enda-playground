#%%
from dataclasses import asdict
from datetime import datetime, timedelta

import xarray as xr
from xarray_dataclasses import asdataarray

from cf_classes.time_series import (
    asstationvariable,
    astimevariable,
    astimearray,
    TimeSeriesCoord,
)

# from cf_classes.utils.common import WGS1984
from cf_classes.utils.attributes import TimeAttrs, VariableAttrs, LongitudeAttrs
from cf_classes.dims import TIME, DIMLESS
from attrs import asdict

#%%
t = astimevariable([datetime(1999, 10, 4)], attrs=asdict(TimeAttrs()))
#%%
d = xr.Dataset({"time": t, "id": asstationvariable("hei")})
#%
# standard names http://vocab.nerc.ac.uk/collection/P07/current/
temperature = astimearray(
    name="temperature",
    data=[10, 15],
    coords=TimeSeriesCoord(
        time=xr.Variable(
            TIME, [datetime(1999, 10, 4), datetime(1999, 10, 5)], asdict(TimeAttrs())
        ),
        longitude=xr.Variable(DIMLESS, 10.75, asdict(LongitudeAttrs())),
        latitude=xr.Variable(DIMLESS, 59.95, asdict(LongitudeAttrs())),
    ),
    attrs=VariableAttrs(
        standard_name="sea_water_temperature",
        long_name="Sea water temperature",
        units="degree_Celsius",
    ),
)
#%%
salinity = astimearray(
    name="salinity",
    data=[10, 15],
    coords=TimeSeriesCoord(
         time=xr.Variable(
            TIME, [datetime(1999, 10, 4), datetime(1999, 10, 5)], asdict(TimeAttrs())
        ),
        longitude=xr.Variable(DIMLESS, 10.75, asdict(LongitudeAttrs())),
        latitude=xr.Variable(DIMLESS, 59.95, asdict(LongitudeAttrs())),
    ),
    attrs=VariableAttrs(
        standard_name="sea_water_salinity",
        long_name="Salinity at some place",
        units="1e-3",
    ),
)


#%%
conductivity = astimearray(
    name="conductivity",
    data=[10, 15, 100, None],
    coords=TimeSeriesCoord(
        time=xr.Variable(
            TIME, [datetime(1999, 10, i) for i in range(1,5)], asdict(TimeAttrs())
        ),
        longitude=xr.Variable(DIMLESS, 10.75, asdict(LongitudeAttrs())),
        latitude=xr.Variable(DIMLESS, 59.95, asdict(LongitudeAttrs())),
    ),
    attrs=VariableAttrs(
        standard_name="sea_water_electrical_conductivity",
        long_name="Conductivity at depth",
        units="mS cm-1",
    ),
)

#%%
ds = xr.merge(
    [
        temperature,
        salinity,
        conductivity,
        asstationvariable("Oslo1"),
    ]
)
#%%
ds.attrs = asdict(
    DatasetAttrs(
        title="hei",
        date_created=str(datetime.now()),
        keywords=["hei"],
        station_name="Oslo",
        time_coverage_start=str(ds.time.values[0]),
        time_coverage_end=str(ds.time.values[-1]),
        geospatial_lat_min=float(ds.lat),
        geospatial_lat_max=float(ds.lat),
        geospatial_lon_min=float(ds.lon),
        geospatial_lon_max=float(ds.lon),
    )
)

# %%
ds.conductivity.plot.line("o")
# %%
ds
# %%
ds.to_netcdf("test.nc", unlimited_dims=["time"])
# %%
