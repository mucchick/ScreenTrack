import pandas as pd
import folium
import seaborn as sns
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('location_metrics.csv')

# Convert date strings to datetime objects
df['date'] = pd.to_datetime(df['date'])


# Create the map visualization
def create_location_map(df):
    # Calculate the center point for the map
    center_lat = df['center_lat'].mean()
    center_lon = df['center_lon'].mean()

    # Create a map centered on the average location
    m = folium.Map(location=[center_lat, center_lon], zoom_start=12)

    # Add markers for each day's center location
    for idx, row in df.iterrows():
        # Create popup text with date and distance
        popup_text = f"Date: {row['date'].strftime('%Y-%m-%d')}\nDistance: {row['total_distance_km']:.2f} km"

        # Add marker with popup
        folium.CircleMarker(
            location=[row['center_lat'], row['center_lon']],
            radius=5,
            popup=popup_text,
            color='blue',
            fill=True,
            fill_color='blue'
        ).add_to(m)

    # Save the map
    m.save('average_locations_map.html')


# Create the distance visualization
def create_distance_plot(df):
    plt.figure(figsize=(12, 6))

    # Create the main distance plot
    sns.set_style("whitegrid")

    # Create a line plot with points
    ax = sns.lineplot(data=df, x='date', y='total_distance_km', marker='o')

    # Calculate rolling average (7-day window)
    df['rolling_avg'] = df['total_distance_km'].rolling(window=7, min_periods=1).mean()

    # Add rolling average line
    sns.lineplot(data=df, x='date', y='rolling_avg', color='red', label='7-day average')

    # Customize the plot
    plt.title('Daily Distance Covered Over Time', pad=20)
    plt.xlabel('Date')
    plt.ylabel('Distance (km)')

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45)

    # Add summary statistics as text
    stats_text = f"Total Distance: {df['total_distance_km'].sum():.1f} km\n"
    stats_text += f"Daily Average: {df['total_distance_km'].mean():.1f} km\n"
    stats_text += f"Max Distance: {df['total_distance_km'].max():.1f} km"

    plt.text(0.02, 0.98, stats_text,
             transform=plt.gca().transAxes,
             verticalalignment='top',
             bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

    # Adjust layout to prevent label cutoff
    plt.tight_layout()

    # Save the plot
    plt.savefig('distance_analysis.png', dpi=300, bbox_inches='tight')
    plt.close()


# Generate both visualizations
create_location_map(df)
create_distance_plot(df)

print("Visualizations have been created:")
print("1. average_locations_map.html - Interactive map showing average daily locations")
print("2. distance_analysis.png - Distance analysis plot with trends and statistics")