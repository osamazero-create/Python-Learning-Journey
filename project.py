import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('tips')
data = df['total_bill']

mean_val = data.mean()
median_val = data.median()
mode_val = data.mode()[0]
range_val = data.max() - data.min()
variance_val = data.var()
std_val = data.std()

print("=" * 50)
print("STATISTICAL RESULTS")
print("=" * 50)
print(f"Mean: {mean_val:.2f}")
print(f"Median: {median_val:.2f}")
print(f"Mode: {mode_val:.2f}")
print(f"Range: {range_val:.2f}")
print(f"Variance: {variance_val:.2f}")
print(f"Standard Deviation: {std_val:.2f}")
print("=" * 50)

plt.ion()

plt.figure()
sns.barplot(x=df['day'], y=df['total_bill'])
plt.title('Bar Plot - Total Bill by Day')
plt.xlabel('Day')
plt.ylabel('Total Bill')
plt.show()

plt.figure()
sns.scatterplot(x=df['total_bill'], y=df['tip'])
plt.title('Scatter Plot - Total Bill vs Tip')
plt.xlabel('Total Bill')
plt.ylabel('Tip')
plt.show()

plt.figure()
plt.hist(data, bins=15, edgecolor='black', color='skyblue')
plt.title('Histogram - Distribution of Total Bill')
plt.xlabel('Total Bill')
plt.ylabel('Frequency')
plt.show()

plt.figure()
sns.boxplot(y=data, color='lightgreen')
plt.title('Box Plot - Total Bill')
plt.ylabel('Total Bill')
plt.show()

plt.figure()
day_counts = df['day'].value_counts()
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
plt.pie(day_counts, labels=day_counts.index, autopct='%1.1f%%', 
        startangle=90, colors=colors, explode=(0.05, 0.05, 0.05, 0.05))
plt.title('Pie Chart - Distribution by Day')
plt.show()

plt.ioff()
plt.show(block=True)