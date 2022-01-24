#%%
from cfxarray.datasets import SampleDataSet
from datetime import datetime, timedelta
import numpy as np
# %%
ds_empty = SampleDataSet.empty({"time": 0})
# %%
ds_empty
# %%
ds = SampleDataSet.new(
    temperature=[1, 2, 3],
    salinity=[1, None, 3],
    lat=[59.95, 59.85, 59.75],
    lon=[10.75, 10.65, 10.55],
    time=np.arange(datetime(1995, 7, 1), datetime(1995, 7, 4), timedelta(days=1)),
    trajectory_id="hei",
)
# %%
ds
# %%
