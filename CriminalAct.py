import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

CA2020 = pd.read_csv("NIBRS_CRIMINAL_ACT_2020.csv")["criminal_act_id"].value_counts()
CA2021 = pd.read_csv("NIBRS_CRIMINAL_ACT_2021.csv")["criminal_act_id"].value_counts()
CA2022 = pd.read_csv("NIBRS_CRIMINAL_ACT_2022.csv")["criminal_act_id"].value_counts()


print(CA2020[9])
print(CA2021)
print(CA2022)