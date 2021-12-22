#%%
import cf
# %%
samples = cf.read("202112_E39_G_Halsafjorden_ctd.nc")

# %%
samples[0].properties()
# %%
for s in samples:
    s.data = []
# %%
# %%
with open("testnc.py", "w") as f:
    f.write(samples[0].creation_commands())

# %%
