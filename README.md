# __ScreenTrack__
## _Predicting Digital Behavior through Location and Environmental Patterns_
### Motivation
I am working on this project to gain deeper insights about my screen time patterns and their relationship with my physical environment. By analyzing the all of my location data, weather conditions, and screen time, I aim to understand where and under what circumstances I tend to spend more time on my phone. The primary motivation is my desire to reduce excessive screen time by identifying specific patterns that lead to my increased screen time. Understanding these patterns could provide insights for me to develop better digital habits.
Potential insights this project could reveal:
* Whether I use phone more at home or not.
* Weather conditions that trigger increased screen time.
* The relationship between movement patterns and screen time.
### Datasets
1. __Screen Time Data__
  * _Collection Methods_
    * IOS Screen Time
    * Daily CSV updates by hand
  * _Time Period_
    * Past 38 days
  * _Metrics_
    * Total screen time
2. __Location Data__
  * _Collection Methods_
    * Google Timeline Data
    * Gathered by Google Takeout
  * _Time Period_
    * Past 38 days
  * _Metrics_
    * Average Location of the Day
    * Daily Distance Traveled
3. __Weather Data__
  * _Collection Methods_
    * OpenWeatherMap API
  * _Time Period_
    * Past 38 days
  * _Metrics_
    * Temperature
    * Precipitation
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
     * Daily patterns
   * _Basic Visualizations_
     * Location maps
     * Correlation plots
     * Time series analysis charts

3. __Machine Learning Implementation__
   * _Feature Engineering_
     * Time-based features
     * Weather indicators
     * Mobility indicators
   * _Model Development_
     * Screen time prediction models
     * Pattern recognition
     * Factor importance analysis

4. __Insights & Visualization__
   * _Final Analysis_
     * Interactive usage pattern maps
     * Trend identification
     * Behavior pattern reports

