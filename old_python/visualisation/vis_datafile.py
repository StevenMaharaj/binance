import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("darkgrid")
path = "../data/datafile.csv"
df = pd.read_csv(path)
print(df.head())
df.plot(x = 'Close_time',y = 'Close')
plt.xlabel('time stamp')
plt.ylabel('Close Price')
plt.show()

# print(df.columns)