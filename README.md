# Retail Sales Forecasting Project

This project aimed to predict department-wide sales for 45 different stores using historical sales data, store information, and additional features related to stores, departments, and regional activity. The objective was to model the effects of markdowns on holiday weeks and provide actionable insights for business impact.

## Table of Contents
- [Objective](#objective)
- [Data Overview](#data-overview)
- [Initial Insights](#initial-insights)
- [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
- [Modeling Approach](#modeling-approach)
- [Model Performance](#model-performance)
- [Conclusion](#conclusion)
- [How to Use](#how-to-use)
- [Acknowledgments](#acknowledgments)
- [License](#license)

## Objective

The objective of this project was to predict department-wide sales for 45 different stores. The goal was to model the effects of markdowns on holiday weeks and provide actionable insights to prioritize business impact.

## Data Overview

- **Stores Dataset**: Anonymized information about the 45 stores, including store ID, type (A, B, C), and size.
- **Features Dataset**: Additional data related to the store, department, and regional activity for specific dates, including temperature, fuel price, promotional markdowns (MarkDown1-5), consumer price index (CPI), unemployment rate, and information about special holiday weeks.
- **Sales Dataset**: Historical sales data covering three years, including store ID, department ID, week start date, weekly sales, and information about special holiday weeks.

## Initial Insights

- **Temperature**: Sales data is distributed across seasons, with outliers at low temperatures.
- **Fuel Price**: Skewed data with limited outliers.
- **Markdowns**: Skewed data with outliers. No direct correlation between markdowns and sales was observed.
- **CPI and Unemployment**: Both variables showed specific clusters, indicating potential categorization.

## Exploratory Data Analysis (EDA)

- **Seasonal Patterns**: Clear sales spikes were observed during November-December in 2010 and 2011, but this pattern was missing in 2012.
- **Markdowns**: No significant trend between markdowns and sales was found. Assumptions about markdowns being promotions did not hold.

## Modeling Approach

Three different modeling approaches were taken:

- **Raw Data**: Merged all datasets, including markdown values, without additional transformations except replacing missing markdown values with zero.
- **Basic Data**: Merged datasets without markdown columns.
- **Transformed Data**: Applied data transformations, including replacing dates with week numbers, and utilized multiple regression algorithms.

## Model Performance

The models were evaluated using Mean Absolute Error (MAE), Mean Squared Error (MSE), and Root Mean Squared Error (RMSE). The performance of the models was satisfactory, but there is room for further fine-tuning and optimization.

## Conclusion

The project successfully built regression models to predict sales across different stores. While the models performed well, there is potential for improvement through hyperparameter tuning and exploring more advanced algorithms. The insights gained from the analysis provide a foundation for actionable recommendations to enhance business strategies and drive sales.
