#%%
import xarray as xr
# %%
ds = xr.open_mfdataset('./nc/*.nc')
# %%
ds
# %%
ds.to_zarr('zarr/datasets', consolidated=True)
# %%
