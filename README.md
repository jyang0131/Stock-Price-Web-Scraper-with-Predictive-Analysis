# Stock-Price-Web-Scraper-with-Predictive-Analysis
 This project is a comprehensive Python-based tool designed to scrape real-time stock prices from online sources, specifically focusing on Apple Inc. (AAPL). In addition to collecting current market data, the tool leverages historical price data to perform predictive analysis, helping users anticipate future stock price trends.


#Key Features:

#Web Scraping for Real-Time Data: Automatically fetch live stock price updates from trusted financial websites or APIs.
#Historical Data Integration: Gather and process historical stock prices for AAPL to build a comprehensive dataset.
#Predictive Modeling: Utilize machine learning techniques, such as linear regression, ARIMA, or LSTM, to forecast future stock prices based on historical trends and patterns.
#Data Visualization: Generate intuitive graphs and charts for stock trends, historical data, and predictive outputs.
#Customizable Parameters: Allow users to adjust the prediction window (e.g., daily, weekly, monthly) and model settings for more tailored results.
#User-Friendly Interface: Easy-to-navigate dashboard to view scraped data, prediction results, and visualizations.
#Exportable Reports: Save predictions and visualizations as files for further analysis or sharing.

#This tool is perfect for investors, financial analysts, and anyone interested in understanding and predicting stock price movements for Apple Inc. or other stocks.
import yfinance as yf
import pandas as pd
import sqlite3
from tabulate import tabulate

apple = yf.Ticker("AAPL")
apple_share_price_data = apple.history(period="max")

print(apple_share_price_data.head())

apple_deviden = apple.dividends
print(apple_deviden.head())

import matplotlib.pyplot as plt

# Plot the closing price
apple_share_price_data['Close'].plot(figsize=(10,5))
plt.title("Apple Stock Price Over Time")
plt.xlabel("Date")
plt.ylabel("Close Price (USD)")
plt.show()


plt.figure(figsize=(10, 6))
apple_dividends(label='Dividends', color='blue', marker='o')
plt.title('Apple Dividends Over Time')
plt.xlabel('Date')
plt.ylabel('Dividends ($)')
plt.grid(True)
plt.legend()
plt.show()
