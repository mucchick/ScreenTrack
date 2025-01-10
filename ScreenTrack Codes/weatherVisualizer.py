import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the CSV file with semicolon separator, and skip the first row
df = pd.read_csv('weatherData.csv', skiprows=1, sep=';')

# Replace empty values with 0
df = df.fillna(0)

# Convert date to datetime
df['date'] = pd.to_datetime(df['date'])

# Create precipitation bar plot
plt.figure(figsize=(12, 6))
plt.bar(df['date'], df['prcp'], color='skyblue', width=0.8)
plt.title('Daily Precipitation')
plt.xlabel('Date')
plt.ylabel('Precipitation (mm)')

# Only show x-ticks for days with precipitation
rainy_days = df[df['prcp'] > 0]
plt.xticks(rainy_days['date'], rainy_days['date'].dt.strftime('%Y-%m-%d'), rotation=45)

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
# Save precipitation plot
plt.savefig('precipitation_plot.png')
plt.close()

# Create temperature time series plot
plt.figure(figsize=(12, 6))
plt.plot(df['date'], df['tavg'], color='red', marker='o')
plt.title('Daily Average Temperature Over Time')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
# Save temperature plot
plt.savefig('temperature_trend.png')
plt.close()

for column in df.columns:
    print(f"\nColumn: {column}")
    print(f"Mean: {df[column].mean()}")
    print(f"Median: {df[column].median()}")
    print(f"Std: {df[column].std()}")
    print(f"Min: {df[column].min()}")
    print(f"Max: {df[column].max()}")