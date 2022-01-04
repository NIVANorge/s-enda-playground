#%%
from matplotlib import markers
import xarray as xr
from ctd_dataclasses import (
    CTDDatasetAttributes,
    Conductivity,
    Latitude,
    Longitude,
    Salinity,
    WaterTemp,
)
from datetime import datetime
import json
#%%
w_temp = WaterTemp.new(
    #(4m, 8m)
    [(10, 15), (20, 25)],
    time=["1970-01-01T00:00:00.000000000", "1970-01-01T01:00:00.000000000"],
    depth=[4, 8],
)
#%%
sal = Salinity.new(
    [(10, 1500), (15, 2000)],
    time=["1970-01-01T00:00:00.000000000", "1970-01-01T10:00:00.000000000"],
    depth=[4, 8],
)
#%%
con = Conductivity.new(
    [(10, 15), (15, 20)],
    time=["1970-01-01T00:00:00.000000000", "1970-01-01T10:00:00.000000000"],
    depth=[4, 8],
)
#%%
ds = xr.merge([w_temp, sal, con])
#%%
ds.attrs = CTDDatasetAttributes("hei", str(datetime.now()), keywords=["hei"]).__dict__
#%%
ds.to_netcdf('test.nc')
#%%
ds.sel(depth=4).salinity.plot.line('o')

# %%
ds_e39 = xr.open_dataset('https://thredds.met.no/thredds/dodsC/obs/buoy-svv-e39/2022/01/202201_E39_G_Halsafjorden_ctd.nc')
# %%
ds_sar = xr.open_dataset("http://opendap1.nodc.no/thredds/dodsC/physics/point/yearly/58JH_CTD_2020.nc")
# %%
ds_sar

# %%
