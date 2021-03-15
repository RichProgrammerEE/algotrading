#%%
import pickle
import pandas as pd
import pyfolio as pf

#%%
def process_performance(fname):
    perf = pd.read_pickle(f"{fname}.pickle")
    perf.to_csv(f"{fname}.csv")
    perf.index = perf.index.normalize()
    return perf
# %%
perf = process_performance("perf")
# %%
