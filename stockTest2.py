import yfinance as yf

df = yf.download(tickers="UBER", period='1d', interval='1m')

for index, row in df.iterrows():
    print(row['Open'])