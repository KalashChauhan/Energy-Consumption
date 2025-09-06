# Energy-Consumption
Rising household energy consumption is a major sustainability challenge. Many people are unaware of which appliances consume the most power and how to optimize their usage. This project explores a real dataset of household appliance energy consumption to generate insights for energy efficiency and sustainable living.

DATASET Source
Source: Kaggle-Appliances energy prediction
Features include: Appliance consumption, lights, temperature, humidity, weather, and time.

Week 1 Objectives
1.Import dataset.
2.Explore with .info(), .describe(), .isnull().sum().
3.Document initial understanding of the data.

Week 2 Objectives
1.Preprocessing Steps 
1.1: Dataset Cleaning
Checked for missing values and handled them appropriately.
Converted the date column into hour and day-of-week features for better time-based analysis.

1.2:Feature & Target Separation
Target Variable: Appliances (energy consumption).
Features: All other environmental and household parameters (temperature, humidity, weather, etc.).

1.3:Feature Scaling
Standardized input features using StandardScaler to ensure all variables are on the same scale.

2.Model Training
2.1: Linear Regression
A baseline model to establish fundamental performance.
Helps understand linear relationships between features and energy consumption.

2.2:Random Forest Regressor
An ensemble learning method capable of handling non-linear relationships.
Provides feature importance insights.

