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