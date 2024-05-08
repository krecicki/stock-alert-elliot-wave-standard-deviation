'''
This script will:
Open the nasdaqlisted.txt file and read each line.
Skip the header line that contains the column names.
Split each line by the pipe symbol (|) and check if the sixth element (ETF column) is ‘N’ to filter out ETFs, assuming you’re only interested in common stocks.
Add the ticker symbol to the tickers list.
For each ticker in the list, it will download the last 7 days of closing prices using yfinance.
It will then check if the last closing price is more than 2 standard deviations away from the mean and add it to the outliers list if it is.
'''
    
import yfinance as yf
import pandas as pd

# Step 1: Parse the file to get the list of tickers
tickers = []
with open('nasdaqlisted.txt', 'r') as file:
    next(file)  # Skip the header line
    for line in file:
        split_line = line.strip().split('|')
        if split_line[6] == 'N':  # Filter out ETFs
            tickers.append(split_line[0])

# Function to check if the price is ±2σ from the mean
def is_outlier(prices):
    mean = prices.mean()
    std_dev = prices.std()
    lower_bound = mean - 2 * std_dev
    upper_bound = mean + 2 * std_dev
    return prices.iloc[-1] < lower_bound or prices.iloc[-1] > upper_bound

# Step 2 & 3: Download historical data and analyze
outliers = []
for ticker in tickers:
    try:
        # Download last 7 days of data
        data = yf.download(ticker, period='7d')
        if is_outlier(data['Close']):
            outliers.append(ticker)
    except Exception as e:
        print(f"Error downloading data for {ticker}: {e}")

# Print the list of outlier tickers
print("Tickers that are ±2σ from the mean:", outliers)
