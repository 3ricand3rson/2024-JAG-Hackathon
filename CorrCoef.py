import numpy as np
import pandas as pd

array1 = np.arange(1, 100)
array2 = []

for x in array1:
	array2.append(np.random.randint(1,100))

matrix = np.corrcoef(array1, array2)

print(matrix)
