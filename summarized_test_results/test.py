import pandas as pd

import scikit_posthocs as sp


data = pd.read_csv("tmp.csv")
data = [data[key] for key in data]

# Perform Scott-Knott test
wc = sp.posthoc_wilcoxon(data)
print("wilcoxon Results:")
print(wc)
