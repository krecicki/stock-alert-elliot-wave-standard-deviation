import yfinance as yf
import pandas as pd

# Function to calculate the Elliott Wave Oscillator (EWO)
def calculate_ewo(data, short_window=5, long_window=35):
    ewo = data['Close'].rolling(window=short_window).mean() - data['Close'].rolling(window=long_window).mean()
    print(f"EWO calculated with short window {short_window} and long window {long_window}")
    return ewo

# Function to check for divergence
def check_divergence(data, ewo):
    # Assuming we're looking for divergence in the last three data points
    price_peaks = data['Close'][-3:].tolist()
    ewo_peaks = ewo[-3:].tolist()
    print(f"Price peaks for divergence check: {price_peaks}")
    print(f"EWO peaks for divergence check: {ewo_peaks}")

    # Check for bearish divergence (price is up, EWO is down)
    if price_peaks[-1] > price_peaks[-2] and ewo_peaks[-1] < ewo_peaks[-2]:
        print("Bearish divergence detected")
        return 'bearish'
    # Check for bullish divergence (price is down, EWO is up)
    elif price_peaks[-1] < price_peaks[-2] and ewo_peaks[-1] > ewo_peaks[-2]:
        print("Bullish divergence detected")
        return 'bullish'
    else:
        print("No divergence detected")
        return 'none'

# Function to calculate if the current price is -2σ or +2σ
def check_sigma(data):
    # Calculate the mean and standard deviation of the closing prices
    mean_price = data['Close'].mean()
    std_dev = data['Close'].std()
    print(f"Mean price: {mean_price}, Standard Deviation: {std_dev}")

    # Get the most recent closing price
    current_price = data['Close'].iloc[-1]
    print(f"Current price: {current_price}")

    # Calculate the -2σ and +2σ thresholds
    lower_bound = mean_price - (2 * std_dev)
    upper_bound = mean_price + (2 * std_dev)
    print(f"Lower bound (-2σ): {lower_bound}, Upper bound (+2σ): {upper_bound}")

    # Check if the current price is beyond -2σ or +2σ
    if current_price < lower_bound:
        print("Current price is below -2σ. Buy signal.")
        return 'buy'
    elif current_price > upper_bound:
        print("Current price is above +2σ. Sell signal.")
        return 'sell'
    else:
        print("Current price is within bounds. Hold signal.")
        return 'hold'

# Function to fetch historical stock data
def fetch_data(stock_ticker, period="1y", interval="1d"):
    print(f"Fetching data for {stock_ticker} with period {period} and interval {interval}")
    try:
        data = yf.download(stock_ticker, period=period, interval=interval)
        print("Data fetched successfully")
        return data
    except Exception as e:
        print(f"Error fetching data for {stock_ticker}: {e}")
        return pd.DataFrame()

# Main function to analyze the stock ticker
def analyze_stock(stock_ticker):
    print(f"Analyzing stock: {stock_ticker}")
    # Fetch historical data for the stock
    data = fetch_data(stock_ticker)

    # Check if data is empty
    if data.empty:
        print("No data fetched. Exiting analysis.")
        return f"No data fetched for {stock_ticker}. Cannot perform analysis."

    # Calculate EWO
    ewo = calculate_ewo(data)

    # Check for divergence
    divergence = check_divergence(data, ewo)

    # Check sigma
    sigma_status = check_sigma(data)

    # Decision making
    action = 'Hold'  # Default action
    if sigma_status == 'buy' and divergence == 'bullish':
        print("Buy signal based on sigma and divergence")
        action = 'Buy'
    elif sigma_status == 'sell' and divergence == 'bearish':
        print("Sell signal based on sigma and divergence")
        action = 'Sell'
    else:
        print("Hold based on sigma and divergence")

    return f"{stock_ticker}: {action}"

# Example usage
ticker = "AAPL"  # Replace with any stock ticker
analysis_result = analyze_stock(ticker)
print(analysis_result)
