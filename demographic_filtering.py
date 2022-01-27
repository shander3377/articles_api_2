import pandas as pd
import numpy as np

df = pd.read_csv('articlces.csv')
df = df.sort_values('total_events', ascending=False)
output = df[["url", "text", "title", "lang" "total_events"]].head(20).values.tolist()