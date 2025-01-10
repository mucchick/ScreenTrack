import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from math import radians, sin, cos, sqrt, atan2
import numpy as np

# Constants for home location
HOME_LAT = 40.831105
HOME_LON = 29.316890


def calculate_distance(lat1, lon1, lat2, lon2):
    """Calculate distance between two points using Haversine formula"""
    R = 6371  # Earth's radius in kilometers

    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c

    return distance


def calculate_correlation(df1, df2, col1, col2):
    """Calculate correlation between two columns from different dataframes"""
    merged = pd.merge(df1, df2, on='date', how='outer')  # Use outer merge to get all dates
    # Fill missing values with 0
    merged = merged.fillna(0)

    # Debug print
    print(f"\nCalculating correlation between {col1} and {col2}")
    print(f"Number of matched rows: {len(merged)}")
    print(f"Sample of merged data:")
    print(merged[[col1, col2]].head())

    correlation = abs(merged[col1].corr(merged[col2]))
    print(f"Correlation value: {correlation}")
    return correlation


def main():
    try:
        # 1. Read location metrics (comma-separated)
        location_df = pd.read_csv('location_metrics.csv').fillna(0)
        print("\nLocation data sample:")
        print(location_df.head())

        # 2. Read screen time (semicolon-separated)
        screen_df = pd.read_csv('screen_time.csv', sep=';').fillna(0)
        print("\nScreen time data sample:")
        print(screen_df.head())

        # 3. Read weather data (process the export column)
        raw_weather = pd.read_csv('weatherData.csv')

        # Split the export column by semicolon and create new dataframe
        weather_data = []
        for row in raw_weather['export'].iloc[1:]:  # Skip header row
            split_row = row.split(';')
            weather_data.append({
                'date': split_row[0],
                'avg_temp': float(split_row[1]) if split_row[1] != '' else 0,
                'precipitation': float(split_row[2]) if split_row[2] != '' else 0
            })

        weather_df = pd.DataFrame(weather_data).fillna(0)
        print("\nProcessed weather data sample:")
        print(weather_df.head())

        # Calculate distance from home for each location
        location_df['distance_from_home'] = location_df.apply(
            lambda row: calculate_distance(
                HOME_LAT, HOME_LON,
                row['center_lat'], row['center_lon']
            ), axis=1
        )

        # Calculate correlations with screen time
        correlations = {
            'Distance from Home': calculate_correlation(
                location_df, screen_df,
                'distance_from_home', 'screen_time'
            ),
            'Total Distance': calculate_correlation(
                location_df, screen_df,
                'total_distance_km', 'screen_time'
            ),
            'Temperature': calculate_correlation(
                weather_df, screen_df,
                'avg_temp', 'screen_time'
            ),
            'Precipitation': calculate_correlation(
                weather_df, screen_df,
                'precipitation', 'screen_time'
            )
        }

        # Create correlation dataframe
        corr_df = pd.DataFrame(list(correlations.items()),
                               columns=['Metric', 'Correlation'])
        corr_df = corr_df.sort_values('Correlation', ascending=True)

        print("\nFinal correlation values:")
        print(corr_df)

        # Create the plot
        plt.figure(figsize=(10, 6))
        sns.set_style("whitegrid")

        # Create horizontal bar plot
        ax = sns.barplot(x='Correlation', y='Metric', data=corr_df,
                         color='#8884d8', orient='h')

        # Customize the plot
        plt.title('Screen Time Correlations', pad=20, fontsize=14)
        plt.xlabel('Correlation Coefficient', fontsize=12)
        plt.ylabel('Metrics', fontsize=12)

        # Add value labels on the bars
        for i, v in enumerate(corr_df['Correlation']):
            ax.text(v, i, f'{v:.3f}', va='center', fontsize=10,
                    color='black', fontweight='bold')

        # Set x-axis limits from 0 to 1
        plt.xlim(0, 1)

        # Add grid lines
        ax.grid(True, axis='x', linestyle='--', alpha=0.7)

        # Add text box with explanation
        plt.figtext(0.02, 0.02,
                    'Correlation coefficient ranges from 0 (no correlation) '
                    'to 1 (perfect correlation).\n'
                    'Values closer to 1 indicate stronger relationships with '
                    'screen time.\n'
                    '• Strong correlation: > 0.5\n'
                    '• Moderate correlation: 0.3 - 0.5\n'
                    '• Weak correlation: < 0.3',
                    fontsize=8, ha='left', va='bottom',
                    bbox=dict(facecolor='white', alpha=0.8, pad=5))

        # Adjust layout to prevent text cutoff
        plt.tight_layout()

        # Save as PNG only
        plt.savefig('screen_time_correlations.png',
                    format='png',
                    bbox_inches='tight',
                    dpi=300)

        print("\nSuccessfully generated 'screen_time_correlations.png'")

    except FileNotFoundError as e:
        print(f"Error: Could not find one or more CSV files: {e}")
    except pd.errors.EmptyDataError:
        print("Error: One or more CSV files are empty")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()