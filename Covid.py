import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('country_wise_latest.xls')

df.plot()

plt.show() 
