import matplotlib.pyplot as plt
import pandas as pd

#add csv file to dataframe
df = pd.read_csv('average_total_rewards.csv')

#create boxplot
lines = df.plot.line()
plt.xlabel("Popularity")
plt.ylabel("Average Total Rewards")
plt.xticks(rotation=30, ha='right')

plt.show()
plt.savefig("average_total_rewards.eps")