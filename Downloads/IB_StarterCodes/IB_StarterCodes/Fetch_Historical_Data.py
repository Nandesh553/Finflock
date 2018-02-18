from ib_insync import *

ib = IB()
ib.connect('127.0.0.1', 7497, clientId=9898)


## Contracts

# Stock('AMD', 'SMART', 'USD')
# Stock('INTC', 'SMART', 'USD', primaryExchange='NASDAQ')
# Forex('EURUSD')
# CFD('IBUS30')
# Future('ES', '20180921', 'GLOBEX')
# Option('SPY', '20170721', 240, 'C', 'SMART')
# Bond(secIdType='ISIN', secId='US03076KAA60')




## Fetches previous 30 Days data for particular Forex
contract = Forex('EURUSD')
bars = ib.reqHistoricalData(contract, endDateTime='', durationStr='30 D',
        barSizeSetting='1 hour', whatToShow='MIDPOINT', useRTH=True)

# convert to pandas dataframe:
df = util.df(bars)
print("############################################")
print("\n\nEURUSD FOREX Previous 1 Month Data...\n\n")
print("Top 5 Rows\n")
print(df[['date', 'open', 'high', 'low', 'close']].head())
print("\nLast 5 Rows\n")
print(df[['date', 'open', 'high', 'low', 'close']].tail())
print("\n\n\n\n")

contract = Forex('GBPUSD')
bars = ib.reqHistoricalData(contract, endDateTime='', durationStr='30 D',
        barSizeSetting='1 hour', whatToShow='MIDPOINT', useRTH=True)

# convert to pandas dataframe:
df = util.df(bars)
print("############################################")
print("\n\nGBPUSD FOREX Previous 1 Month Data...\n\n")
print("Top 5 Rows\n")
print(df[['date', 'open', 'high', 'low', 'close']].head())
print("\nLast 5 Rows\n")
print(df[['date', 'open', 'high', 'low', 'close']].tail())
print("\n\n\n\n")

contract = Forex('USDJPY')
bars = ib.reqHistoricalData(contract, endDateTime='', durationStr='30 D',
        barSizeSetting='1 hour', whatToShow='MIDPOINT', useRTH=True)

# convert to pandas dataframe:
df = util.df(bars)
print("############################################")
print("\n\nUSDJPY FOREX Previous 1 Month Data...\n\n")
print("Top 5 Rows\n")
print(df[['date', 'open', 'high', 'low', 'close']].head())
print("\nLast 5 Rows\n")
print(df[['date', 'open', 'high', 'low', 'close']].tail())
print("\n\n\n\n")

contract = Forex('CHFUSD')
bars = ib.reqHistoricalData(contract, endDateTime='', durationStr='30 D',
        barSizeSetting='1 hour', whatToShow='MIDPOINT', useRTH=True)

# convert to pandas dataframe:
df = util.df(bars)
print("############################################")
print("\n\nCHFUSD FOREX Previous 1 Month Data...\n\n")
print("Top 5 Rows\n")
print(df[['date', 'open', 'high', 'low', 'close']].head())
print("\nLast 5 Rows\n")
print(df[['date', 'open', 'high', 'low', 'close']].tail())
print("\n\n\n\n")

