#%%
from dataclasses import asdict
from datetime import datetime, timedelta
import numpy as np

import xarray as xr
from xarray_dataclasses import asdataarray, asdataset

from cf_classes.time_series import StationId, TimeSeriesAttrs
from cf_classes.dimless import Latitude, Longitude, Altitude
from cf_classes.time import DataVarByTime
from cf_classes.common import WGS1984

#%%
# standard names http://vocab.nerc.ac.uk/collection/P07/current/
temperature = DataVarByTime(
    name="temperature",
    standard_name="sea_water_temperature",
    long_name="Sea water temperature",
    units="degree_Celsius",
    data=[10, 15],
    time=["1970-01-01T00:00:00", "1970-01-01T01:00:10"],
)
#%%
salinity = DataVarByTime(
    name="salinity",
    standard_name="sea_water_salinity",
    long_name="Salinity at some place",
    units="1e-3",
    data=[10, 1500, 15000, 15, 2000, 20000],
    time=np.arange(datetime(1995, 7, 1), datetime(1995, 7, 7), timedelta(days=1)),
)
#%%
conductivity = DataVarByTime(
    name="conductivity",
    standard_name="sea_water_electrical_conductivity",
    long_name="Conductivity at depth",
    units="mS cm-1",
    data=[10, 15, 56],
    time=[
        "1970-01-01T00:00:00",
        "1970-01-01T10:00:00",
        "1980-01-01T10:00:00",
    ],
)
#%%
ds = xr.merge(
    [
        asdataarray(d)
        for d in [
            temperature,
            salinity,
            conductivity,
            WGS1984(),
            Latitude(59.95),
            Longitude(10.75),
            Altitude(5),
            StationId("Oslo1"),
        ]
    ]
)
#%%
ds.attrs = asdict(
    TimeSeriesAttrs(
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
ds.salinity.plot.line("o")
# %%
ds
# %%
