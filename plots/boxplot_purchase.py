import matplotlib.pyplot as plt
import pandas as pd

#add csv file to dataframe
df = pd.read_csv('rewards_on_purchase-averages_purchase.csv')

# df = df.div(1000)

#create boxplot
boxplot = df.boxplot(figsize = (10,4), grid = False, showfliers = False)
plt.xlabel("API calls")
plt.ylabel("API call delay (seconds)")
plt.xticks(rotation=30, ha='right')
plt.tight_layout()

plt.show()
plt.savefig("purchase_rewards.eps")