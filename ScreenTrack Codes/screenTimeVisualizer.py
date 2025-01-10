import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('screen_time.csv', sep=';')

plt.figure(figsize=(15, 6))

plt.bar(df['date'], df['screen_time'])

plt.title('Screen Time Over Time')
plt.xlabel('Date')
plt.ylabel('Screen Time (minutes)')

plt.xticks(rotation=45, ha='right')
plt.grid(True, axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()

plt.savefig('screen_time_barchart.png', dpi=300, bbox_inches='tight')
plt.close()

print("\nScreen Time Statistics:")
print(df['screen_time'].describe())


