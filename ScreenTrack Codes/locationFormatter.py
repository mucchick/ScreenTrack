import json
from datetime import datetime, date
import pandas as pd
import numpy as np
from geopy.distance import geodesic


def extract_coordinates(entry):
    """Extract coordinates from either timelinePath or visit/activity."""
    coords = []

    # Try to get coordinates from visit or activity
    if 'visit' in entry:
        if 'topCandidate' in entry['visit'] and 'placeLocation' in entry['visit']['topCandidate']:
            loc = entry['visit']['topCandidate']['placeLocation']
            if loc.startswith('geo:'):
                lat, lon = map(float, loc[4:].split(','))
                coords.append((lat, lon))
    elif 'activity' in entry:
        if 'start' in entry['activity'] and entry['activity']['start'].startswith('geo:'):
            lat, lon = map(float, entry['activity']['start'][4:].split(','))
            coords.append((lat, lon))
        if 'end' in entry['activity'] and entry['activity']['end'].startswith('geo:'):
            lat, lon = map(float, entry['activity']['end'][4:].split(','))
            coords.append((lat, lon))

    return coords


def process_location_data(data):
    daily_stats = {}

    for entry in data:
        try:
            # Parse the date
            entry_date = datetime.strptime(entry['startTime'].split('+')[0],
                                           '%Y-%m-%dT%H:%M:%S.%f').date()

            # Initialize daily stats if needed
            if entry_date not in daily_stats:
                daily_stats[entry_date] = {
                    'coordinates': [],
                    'total_distance': 0.0
                }

            # Extract coordinates
            coords = extract_coordinates(entry)
            if coords:
                daily_stats[entry_date]['coordinates'].extend(coords)

                # Calculate distance if we have multiple points
                if len(coords) > 1:
                    for i in range(len(coords) - 1):
                        daily_stats[entry_date]['total_distance'] += geodesic(coords[i], coords[i + 1]).kilometers

        except Exception as e:
            print(f"Error processing entry for {entry.get('startTime', 'unknown date')}: {str(e)}")
            continue

    # Process daily stats into final format
    final_stats = []
    for entry_date, stats in daily_stats.items():
        if not stats['coordinates']:
            continue

        coordinates = stats['coordinates']
        lats, lons = zip(*coordinates)

        # Calculate area
        area = (max(lats) - min(lats)) * (max(lons) - min(lons))

        # Calculate unique locations (rounded to 3 decimal places)
        unique_locations = len(set([f"{lat:.3f},{lon:.3f}" for lat, lon in coordinates]))

        final_stats.append({
            'date': entry_date,
            'total_distance_km': round(stats['total_distance'], 2),
            'center_lat': round(np.mean(lats), 6),
            'center_lon': round(np.mean(lons), 6),
            'location_density': round(unique_locations / area if area > 0 else 0, 4)
        })

    # Create DataFrame and sort by date
    df = pd.DataFrame(final_stats)
    df = df.sort_values('date')

    # Export to CSV
    df.to_csv('location_metrics.csv', index=False)
    return df


def main():
    input_file = 'raw_timeline_data.json'

    try:
        # Read the JSON file
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        location_data = data

        result_df = process_location_data(location_data)

        print(f"Processing complete! Results saved to location_metrics.csv")
        print("\nFirst few rows of processed data:")
        print(result_df.head())

    except FileNotFoundError:
        print(f"Error: Could not find the file {input_file}")
    except json.JSONDecodeError:
        print(f"Error: The file {input_file} is not valid JSON")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")


if __name__ == "__main__":
    main()