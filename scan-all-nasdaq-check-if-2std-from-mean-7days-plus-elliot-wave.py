# Search over all tickers on NASDAQ list -+2 STD from mean 7 days ago + EWO -- go to ftp.nasdaqtrader.com and login anonymously 
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

# Function to calculate the Elliott Wave Oscillator (EWO)
def calculate_ewo(data):
    short_sma = data['Close'].rolling(window=5).mean()
    long_sma = data['Close'].rolling(window=35).mean()
    ewo = short_sma - long_sma
    return ewo

# Function to check for divergence
def has_divergence(data, ewo):
    last_price = data['Close'].iloc[-1]
    previous_price = data['Close'].iloc[-2]
    
    last_ewo = ewo.iloc[-1]
    previous_ewo = ewo.iloc[-2]
    
    # Check for bullish divergence (price is lower, but EWO is higher)
    bullish_divergence = last_price < previous_price and last_ewo > previous_ewo
    
    # Check for bearish divergence (price is higher, but EWO is lower)
    bearish_divergence = last_price > previous_price and last_ewo < previous_ewo
    
    return bullish_divergence or bearish_divergence

# Function to check if the price is ±2σ from the mean
def is_outlier(prices):
    mean = prices.mean()
    std_dev = prices.std()
    lower_bound = mean - 2 * std_dev
    upper_bound = mean + 2 * std_dev
    return prices.iloc[-1] < lower_bound or prices.iloc[-1] > upper_bound

# Step 2 & 3: Download historical data and analyze
outliers_with_divergence = []
for ticker in tickers:
    try:
        # Download last 7 days of data
        data = yf.download(ticker, period='7d')
        ewo = calculate_ewo(data)
        if is_outlier(data['Close']) and has_divergence(data, ewo):
            outliers_with_divergence.append(ticker)
    except Exception as e:
        print(f"Error downloading data for {ticker}: {e}")

# Print the list of tickers that meet both conditions
print("Tickers that are ±2σ from the mean and have Elliott Wave divergence:", outliers_with_divergence)
