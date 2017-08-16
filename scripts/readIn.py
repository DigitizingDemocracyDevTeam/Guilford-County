import pandas as pd
import matplotlib.pyplot as plt

addressPoints = pd.read_csv('data/GIS/AddressPoints.csv', sep = ',', keep_default_na = False, low_memory = False)

print(addressPoints.head())
print(addressPoints.shape)

