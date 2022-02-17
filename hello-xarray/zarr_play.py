#%%
import gcsfs
import xarray as xr
import zarr

# %%
ds = xr.open_mfdataset("test.nc")
# %%
ds
# %%
gcs_path = "gs://niva-test-datasets/test"
gcs = gcsfs.GCSFileSystem()
store = gcsfs.GCSMap(root=gcs_path, gcs=gcs)
#%%
compressor = zarr.Blosc(cname="zstd")
encoding = {vname: {"compressor": compressor} for vname in ds.data_vars}
ds.to_zarr(store=store, consolidated=True)
# %%
ds = xr.open_zarr("gs://niva-test-datasets/test")
# %%
ds
# %%
