# Colab Notebook
https://colab.research.google.com/drive/1pceLs9xdsibCqw7rO2Uedh-owSQPEHrF?usp=sharing

# stock-alert-elliot-wave-standard-deviation
Using Elliot wave and 2σ/+2σ standard deviations to notify when to buy, sell hold individual stock tickers.

This script will output the stock ticker’s current status regarding the -2σ/+2σ range and whether there is any divergence detected according to the EWO. Remember to replace "AAPL" with the ticker symbol you want to analyze. Before running the script, ensure you have the pandas and yfinance libraries installed in your Python environment.

# Back story on this quant indicator 
Someone on Twitter who does quant trading told me, "Asness says anything that has a price can be trend followed. at fundamental level buying from -2σ and selling over +2σ works well on commodities. you can combine it with EWO divergence, seasonality, calendar or day of the week anomalies etc. depending on your trading horizon."

Cliff Asness, a notable figure in finance, suggests that trend following can be applied to any asset that has a price. This is based on the idea that prices tend to move in trends over time, and these trends can be capitalized on through strategic buying and selling.

At a fundamental level, buying at -2 standard deviations (σ) and selling over +2σ refers to a statistical approach where you enter a trade when the price is significantly below its mean (suggesting it’s undervalued) and exit when it’s significantly above its mean (indicating it’s overvalued). This is particularly noted to work well with commodities, which often exhibit mean-reverting behavior.

The Elliott Wave Oscillator (EWO) divergence is a technical analysis tool that measures the difference between a short-term and a long-term moving average, and divergence occurs when the price trend and the EWO trend move in opposite directions, indicating potential reversals.

Seasonality refers to predictable patterns that occur at certain times of the year, which can affect trading strategies. For example, certain commodities may have price spikes or drops during specific seasons due to supply and demand changes.

Calendar anomalies are patterns associated with specific times of the calendar, such as the weekend effect or the January effect, where stocks tend to perform differently during these periods.

Day of the week anomalies refer to the tendency.


