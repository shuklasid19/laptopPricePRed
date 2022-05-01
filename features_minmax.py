

import pandas  as pd
import numpy as np
import os



df = pd.read_csv('C:\\Users\\sid\\Downloads\\PROGARAMMING\\data_given\\laptop_data.csv')
df =df.iloc[: , 1:12]

overdrive = df.describe()

overdrive.loc[["min", "max"]].to_json("schema_in.json")

print(df.describe)