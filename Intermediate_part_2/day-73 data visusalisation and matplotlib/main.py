import pandas as pd 
import matplotlib.pyplot as plt 


data = pd.read_csv('javascript_data.csv')
data['time'] = pd.to_datetime(data['time'])


plt.figure(figsize=(15,10))
plt.plot(data['time'], data['no'], marker='o', label = data['TagName'][0])


# Customize the chart
plt.title("Tag Counts Over Time", fontsize=16)
plt.xlabel("Time", fontsize=12)
plt.ylabel("Count", fontsize=12)
plt.grid(True)
plt.legend()
plt.xticks(rotation=45)  


plt.tight_layout()
plt.show()