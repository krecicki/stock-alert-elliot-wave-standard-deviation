'''
This script will:
Open the nasdaqlisted.txt file and read each line.
Skip the header line that contains the column names.
Split each line by the pipe symbol (|) and check if the sixth element (ETF column) is ‘N’ to filter out ETFs, assuming you’re only interested in common stocks.
Add the ticker symbol to the tickers list.
For each ticker in the list, it will download the last 7 days of closing prices using yfinance.
It will then check if the last closing price is more than 2 standard deviations away from the mean and add it to the outliers list if it is.
The outliers list is then check for volumes, the top 10 tickers are listed.
'''
# Search over all tickers on NASDAQ list -+2 STD from mean 7 days ago, make 2 outlier lists -- go to ftp.nasdaqtrader.com and login anonymously
import yfinance as yf
import pandas as pd

'''
# Step 1: Parse the file to get the list of tickers if using nasdaqlisted.txt
tickers = []
with open('nasdaqlisted.txt', 'r') as file:
    next(file)  # Skip the header line
    for line in file:
        split_line = line.strip().split('|')
        if split_line[6] == 'N':  # Filter out ETFs
            tickers.append(split_line[0])
'''

# Step 1b: Use this is using commiditieslist.txt
tickers = []
with open('commoditieslist.txt', 'r') as file:
    next(file)  # Skip the header line
    for line in file:
        split_line = line.strip().split('|')
        tickers.append(split_line[0])

# Function to check if the price is -2σ or +2σ from the mean
def check_outliers(prices):
    mean = prices.mean()
    std_dev = prices.std()
    lower_bound = mean - 2 * std_dev
    upper_bound = mean + 2 * std_dev
    if prices.iloc[-1] < lower_bound:
        return 'below'
    elif prices.iloc[-1] > upper_bound:
        return 'above'
    else:
        return 'within'

# Step 2 & 3: Download historical data and analyze
below_outliers = []
above_outliers = []
for ticker in tickers:
    try:
        # Download last 7 days of data
        data = yf.download(ticker, period='7d')
        outlier_type = check_outliers(data['Close'])
        if outlier_type == 'below':
            below_outliers.append(ticker)
        elif outlier_type == 'above':
            above_outliers.append(ticker)
    except Exception as e:
        print(f"Error downloading data for {ticker}: {e}")

# Print the lists of outlier tickers
#print("Tickers more than 2σ below the mean:", below_outliers)
#print("Tickers more than 2σ above the mean:", above_outliers)

# Assuming below_outliers and above_outliers are lists of ticker symbols
tickers = below_outliers + above_outliers

# Retrieve data
data = yf.Tickers(tickers)
market_caps = {}
volumes = {}

for ticker_symbol in tickers:
    ticker_data = data.tickers[ticker_symbol]
    info = ticker_data.info
    volumes[ticker_symbol] = info['volume']

# Sort by market cap and volume
sorted_volumes = sorted(volumes.items(), key=lambda x: x[1], reverse=True)

# Get top 10
top_10_volumes = sorted_volumes[:10]

print("\nTop 10 by Volume:")
for ticker, volume in top_10_volumes:
    print(f"{ticker}: {volume}")

