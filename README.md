# __ScreenTrack__
## _Predicting Digital Behavior through Location and Environmental Patterns_
### Motivation
I am working on this project to gain deeper insights about my screen time patterns and their relationship with my physical environment. By analyzing the all of my location data, weather conditions, and screen time, I aim to understand where and under what circumstances I tend to spend more time on my phone. The primary motivation is my desire to reduce excessive screen time by identifying specific patterns that lead to my increased screen time. Understanding these patterns could provide insights for me to develop better digital habits.
Potential insights this project could reveal:
* Peak screen time locations.
* Weather conditions that trigger increased screen time.
* The relationship between movement patterns and screen time.
### Datasets
1. __Screen Time Data__
  * _Collection Methods_
    * IOS Screen Time
    * Daily CSV updates by hand or OCR
  * _Time Period_
    * Past 2 months
  * _Metrics_
    * App usage duration
    * Total screen time
    * Most used apps
2. __Location Data__
  * _Collection Methods_
    * Google Timeline Data
    * Gathered by Google Takeout
  * _Time Period_
    * Past 2 months
  * _Metrics_
    * Categorized Locations (School, Home, Friends' House etc.)
    * Duration spent
    * Movement Patterns
3. __Weather Data__
  * _Collection Methods_
    * OpenWeatherMap API
  * _Time Period_
    * Past 2 months
  * _Metrics_
    * Temperature
    * Weather Conditions
### Project Plan
1. __Data Collection & Preprocessing__
   * _Data Gathering_
     * Screen time data collection setup
     * Location history export
     * Weather data API integration
   * *Data Cleaning*
     * Merging datasets with timestamps
     * Handling missing values
     * Data format standardization

2. __Exploratory Data Analysis__
   * _Pattern Analysis_
     * Time spent at different locations
     * Screen time variations with weather
     * Daily and weekly patterns
   * _Basic Visualizations_
     * Location heat maps
     * Weather correlation plots
     * Time series analysis charts

3. __Machine Learning Implementation__
   * _Feature Engineering_
     * Location categorization
     * Time-based features
     * Weather indicators
   * _Model Development_
     * Screen time prediction models
     * Pattern recognition
     * Factor importance analysis

4. __Insights & Visualization__
   * _Final Analysis_
     * Interactive usage pattern maps
     * Trend identification
     * Behavior pattern reports
   * _Recommendations_
     * Screen time reduction strategies
     * Pattern-based suggestions
     * Habit improvement insights
