import xarray as xr
#%%
ds_e39 = xr.open_dataset(
    "https://thredds.met.no/thredds/dodsC/obs/buoy-svv-e39/2022/01/202201_E39_G_Halsafjorden_ctd.nc"
)
# %%
ds_sar = xr.open_dataset(
    "http://opendap1.nodc.no/thredds/dodsC/physics/point/yearly/58JH_CTD_2020.nc"
)
# %%
ds_sar