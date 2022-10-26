import matplotlib.pyplot as plt
import pandas as pd

#add csv file to dataframe
df = pd.read_csv('rewards.csv')

# df = df.div(1000)

#create boxplot
boxplot = df.boxplot(figsize = (10,4), grid = False, showfliers = False)
plt.xlabel("Average rewards in ETH for each celebrity")
plt.ylabel("Number of celebrities and transactions")
plt.xticks(rotation=30, ha='right')
plt.tight_layout()

plt.show()
plt.savefig("rewards.eps")