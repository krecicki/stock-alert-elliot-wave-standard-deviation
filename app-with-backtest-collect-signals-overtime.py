'''
This file is also incorrect and does not look back 7 days at the mean to see if a STD change has happene of -+2

This file is for educational purposes of what not to do.
'''

## With list of tickers, singla collecting and backtesting. 
import yfinance as yf
import pandas as pd

# Function to calculate the Elliott Wave Oscillator (EWO)
def calculate_ewo(data, short_window=5, long_window=35):
    ewo = data['Close'].rolling(window=short_window).mean() - data['Close'].rolling(window=long_window).mean()
    return ewo

# Function to check for divergence
def check_divergence(data, ewo):
    # Check for divergence over the entire data set
    price_peaks = data['Close'].tolist()
    ewo_peaks = ewo.tolist()
    divergences = []
    for i in range(2, len(price_peaks)):
        if price_peaks[i] > price_peaks[i-1] and ewo_peaks[i] < ewo_peaks[i-1]:
            divergences.append(('bearish', i))
        elif price_peaks[i] < price_peaks[i-1] and ewo_peaks[i] > ewo_peaks[i-1]:
            divergences.append(('bullish', i))
    return divergences

# Function to calculate if the current price is -2σ or +2σ
def check_sigma(data):
    mean_price = data['Close'].mean()
    std_dev = data['Close'].std()
    lower_bound = mean_price - (2 * std_dev)
    upper_bound = mean_price + (2 * std_dev)
    sigma_events = []
    for i in range(len(data)):
        if data['Close'].iloc[i] < lower_bound:
            sigma_events.append(('buy', i))
        elif data['Close'].iloc[i] > upper_bound:
            sigma_events.append(('sell', i))
    return sigma_events

# Function to fetch historical stock data
def fetch_data(stock_ticker, period="1y", interval="1d"):
    try:
        data = yf.download(stock_ticker, period=period, interval=interval)
        return data
    except Exception as e:
        print(f"Error fetching data for {stock_ticker}: {e}")
        return pd.DataFrame()

# Function to scan tickers for signals and divergences
def scan_tickers(tickers_list, period="1y", interval="1d"):
    signals = []
    for ticker in tickers_list:
        data = fetch_data(ticker, period, interval)
        if data.empty:
            continue

        ewo = calculate_ewo(data)
        divergences = check_divergence(data, ewo)
        sigma_events = check_sigma(data)

        # Combine the signals and divergences
        for sigma_event in sigma_events:
            for divergence in divergences:
                if abs(sigma_event[1] - divergence[1]) <= 5:  # Check if events are within 5 days of each other
                    signals.append({
                        'ticker': ticker,
                        'date': data.index[sigma_event[1]],
                        'sigma_status': sigma_event[0],
                        'divergence': divergence[0],
                        'action': 'Buy' if sigma_event[0] == 'buy' and divergence[0] == 'bullish' else 'Sell'
                    })
    return signals

# Function to perform backtesting
def backtest_signals(signals, initial_capital):
    capital = initial_capital
    for signal in signals:
        if signal['action'] == 'Buy':
            capital *= 1.05  # Assuming a 5% profit on each buy
        elif signal['action'] == 'Sell':
            capital *= 0.95  # Assuming a 5% loss on each sell
    return capital

# Example usage
tickers_list = ["AAPL", "MSFT", "GOOGL"]  # Replace with your list of tickers
initial_capital = 1000  # Initial capital
signals = scan_tickers(tickers_list)
final_capital = backtest_signals(signals, initial_capital)
profitloss = final_capital - initial_capital

# Print the results
print(f"Tickers: {tickers_list}")
#print(f"\n Signals: {signals}")
print(f"\n Profit/Loss: ${profitloss}")
