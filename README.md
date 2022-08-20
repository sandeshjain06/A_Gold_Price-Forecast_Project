# Gold_Price_Forecast_Project

The objective is to understand the underlying structure in your dataset and come up with a suitable forecasting model which can 
effectively forecast gold prices for next 30 days.

- Below is the link of website where we build dataset based on data on this site using web scraping .

- Link where we scrap the data from the website - https://www.goldpriceindia.com/gold-price-january-2011.php

- Link of the dataset - https://github.com/sandeshjain06/Gold_Price-Forecast-Project/blob/main/gold_list.csv

- Link to check the website hosted on heroku platform - https://goldpriceforecast.herokuapp.com/

- Screenshot of the website

![image](https://user-images.githubusercontent.com/91243691/164942814-a6122b2d-888e-47f8-a5a0-6ec6f5bc714c.png)

![image](https://user-images.githubusercontent.com/91243691/164945432-d8d46a06-8e05-4b47-8beb-fd622fc60cac.png)




1. First EDA and Feature Engineering

Steps :

- Dataset consists of 3976 rows(day-wise data) and 2 columns .

- Changed the Date feature format  from “dd/mm/yyyy” to “yyyy/mm/dd”  

- Set the date as index .

- No missing values or Null values were available. 

- Check the Datatype of all features ,object datatype was present so convert it into integer datatype.

- Line plot for Gold price over the years.

![image](https://user-images.githubusercontent.com/91243691/164945411-b7492885-844d-4526-84e1-5809530c5fff.png)

- Box Plot for gold price every years.

![image](https://user-images.githubusercontent.com/91243691/164945441-9254b765-a3e5-437d-b13f-a895a7002fd3.png)


2. Forecast the gold price using Machine Learning 

- List of ML algorithm applied on the time series data.

- Linear Regression , Decision Tree , Random Forests , Gradient Boosting , Ada Boosting.

![image](https://user-images.githubusercontent.com/91243691/164945056-e5e27161-09b7-4dd5-a0a7-a8638a5f3f4d.png)


3. Forecast gold price using Time Series Forecasting

- Time series forecasting in simple words means to forecast or to predict future value(e.g.-stock price) over a period of time.
Collect and study the past observation of time series to develop appropriate model.


- Components of Time Series Modelling 


- Trend -  Upward / Downward				

- Irregularity – Uneven circumstances

- Seasonality – Regular patterns of up and down movements.

- Cyclicity -  Repeating up and down movements


![image](https://user-images.githubusercontent.com/91243691/164945000-caf0e5ad-3abe-4973-a94f-6278c0aef3e7.png)


Time Series Forecasting Algorithms 

- Simple Moving Average , Cumulative Moving Average , Exponential Moving Average 

![image](https://user-images.githubusercontent.com/91243691/164945195-04dfc6fd-605f-44e2-8448-6428891a57da.png)


- Simple Exponential Smoothing , Holt Exponential Smoothing , Exponential Smoothing with additive and multiplicative trend.

![image](https://user-images.githubusercontent.com/91243691/164945201-75b51892-1f91-4321-a71f-41737f48d4de.png)


- Check if the time series given in form of stationary or not.

Technique to covert time series into Stationarity .

1. Rolling Statistics / Moving Average.

2. Differencing and Seasonal Differencing.

3. Log Transformation

Methods to check whether time-series model is Stationarity or   non – Stationarity. 

1. Dickey-Fuller Test and check the p-values.


![image](https://user-images.githubusercontent.com/91243691/164945215-991bf684-9782-4c30-91c8-0415d4c730a5.png)

- Plot the ACF and PACF Plots 

![image](https://user-images.githubusercontent.com/91243691/164945259-f47587b6-d1ed-45f6-a4ef-d1bf7122abf4.png)

-Plot the  ARIMA Model , SARIMA Model

![image](https://user-images.githubusercontent.com/91243691/164945303-3ddfd2a7-fd48-482f-9e56-b37313859a8f.png)


- SARIMA Model predicted price for next 2 years.

![image](https://user-images.githubusercontent.com/91243691/164945385-bfa54d29-d234-4813-9ed7-29b1a55e8bb5.png)

 

















