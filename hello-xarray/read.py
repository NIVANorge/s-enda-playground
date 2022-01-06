#%%
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
#%%
ds_station = xr.open_dataset('https://thredds.met.no/thredds/dodsC/met.no/observations/stations/SN99938.nc')
# %%
ds_station.to_dict(data=False)
# %%
ds_traj = xr.open_dataset('https://podaac-opendap.jpl.nasa.gov/opendap/allData/insitu/L2/saildrone/Baja/saildrone-gen_4-baja_2018-sd1002-20180411T180000-20180611T055959-1_minutes-v1.nc')
# %%
ds_traj.to_dict(data=False)
# %%
ds_traj.obs
# %%
