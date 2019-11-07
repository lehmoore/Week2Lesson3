import pandas as pd


f=pd.read_csv("imdbtitles.csv")
keep_col = [0, 1, 2, 4, 6, 7]
new_f = f[keep_col]
new_f.to_csv("newFile.csv", index=False)