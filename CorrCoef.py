import numpy as np
import pandas as pd

data = pd.read_excel("bigdata.xlsx", sheet_name="Table 19 NIBRS 2022")

Matrix = data.corr()

print(Matrix)
