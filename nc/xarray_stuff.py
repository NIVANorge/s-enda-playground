#%%
import xarray as xr
from ctd_dataclasses import Latitude, Longitude, Salinity
#%%
sal = Salinity.empty((2,2))
#%%
lat = Latitude.empty((2))
long = Longitude.empty(2)
#%%
a = xr.merge([lat, long, sal])
a
# %%
ds_disk = xr.open_dataset("202112_E39_G_Halsafjorden_ctd.nc")

# %%
