import numpy as np
import pandas as pd

data = pd.read_excel("Crimes_Against_Society_Offenses_Offense_Category_by_Location_2022.xlsx", sheet_name="Table 19 NIBRS 2022")

Matrix = data.corr()

print(Matrix)
