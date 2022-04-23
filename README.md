# Gold_Price-Forecast

The objective is to understand the underlying structure in your dataset and come up with a suitable forecasting model which can 
effectively forecast gold prices for next 30 days.

- Below is the link of wesbite where we build dataset based on data on this site using web scraping .

- Link where we scrap the data from the website - https://www.goldpriceindia.com/gold-price-january-2011.php

- Link of the dataset - https://github.com/sandeshjain06/Gold_Price-Forecast-Project/blob/main/gold_list.csv

- Link to check the website hosted on heroku platform - https://goldpriceforecast.herokuapp.com/

- Screenshot of the website

![image](https://user-images.githubusercontent.com/91243691/164942814-a6122b2d-888e-47f8-a5a0-6ec6f5bc714c.png)


1. First EDA and Feature Engineering

Steps :

Dataset consists of 3976 rows(day-wise data) and 2 columns .

Changed the Date feature format  from “dd/mm/yyyy” to “yyyy/mm/dd”  

Set the date as index .

No missing values or Null values were available. 

Check the Datatype of all features ,object datatype was present so convert it into integer datatype.





