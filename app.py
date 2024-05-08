import yfinance as yf
import pandas as pd

# Function to calculate the Elliott Wave Oscillator (EWO)
def calculate_ewo(data, short_window=5, long_window=35):
    ewo = data['Close'].rolling(window=short_window).mean() - data['Close'].rolling(window=long_window).mean()
    return ewo

# Function to check for divergence
def check_divergence(data, ewo):
    # Assuming we're looking for divergence in the last three data points
    price_peaks = data['Close'][-3:].tolist()
    ewo_peaks = ewo[-3:].tolist()
    
    # Check for bearish divergence (price is up, EWO is down)
    if price_peaks[-1] > price_peaks[-2] and ewo_peaks[-1] < ewo_peaks[-2]:
        return 'bearish'
    # Check for bullish divergence (price is down, EWO is up)
    elif price_peaks[-1] < price_peaks[-2] and ewo_peaks[-1] > ewo_peaks[-2]:
        return 'bullish'
    else:
        return 'none'

# Function to calculate if the current price is -2σ or +2σ
def check_sigma(data):
    # Calculate the mean and standard deviation of the closing prices
    mean_price = data['Close'].mean()
    std_dev = data['Close'].std()
    
    # Get the most recent closing price
    current_price = data['Close'].iloc[-1]
    
    # Calculate the -2σ and +2σ thresholds
    lower_bound = mean_price - (2 * std_dev)
    upper_bound = mean_price + (2 * std_dev)
    
    # Check if the current price is beyond -2σ or +2σ
    if current_price < lower_bound:
        return 'buy'
    elif current_price > upper_bound:
        return 'sell'
    else:
        return 'hold'

# Main function to analyze the stock ticker
def analyze_stock(stock_ticker):
    # Fetch historical data for the stock
    data = yf.download(stock_ticker, period="1y")
    
    # Calculate EWO
    ewo = calculate_ewo(data)
    
    # Check for divergence
    divergence = check_divergence(data, ewo)
    
    # Check sigma
    sigma_status = check_sigma(data)
    
    # Decision making
    if sigma_status == 'buy' and divergence == 'bullish':
        action = 'Buy'
    elif sigma_status == 'sell' and divergence == 'bearish':
        action = 'Sell'
    else:
        action = 'Hold'
    
    return f"{stock_ticker}: {action}"

# Example usage
ticker = "AAPL"  # Replace with any stock ticker
analysis_result = analyze_stock(ticker)
print(analysis_result)
