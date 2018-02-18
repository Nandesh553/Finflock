from ib_insync import *
import pandas as pd

ib = IB()
ib.connect('127.0.0.1', 4002, clientId=9898)


a = Forex('EURUSD')
ib.reqMktData(a, '', False, False)
ticker = ib.ticker(a)
ib.sleep(20)
print("\n\n\n")
print(ticker)
print("\n\n\n")
print("\nForex : " , a , "\nTime : " , ticker.time , "\nBid : " , ticker.bid ,"\nAsk : "  , ticker.ask ,"\nbidSize : "  , ticker.bidSize ,"\naskSize : "  , ticker.askSize ,"\nPrice : " , ticker.ticks[0].price)
print("#############################################")

a = Forex('GBPUSD')
ib.reqMktData(a, '', False, False)
ticker = ib.ticker(a)
ib.sleep(20)
print("\n\n\n")
print(ticker)
print("\n\n\n")
print("\nForex : " , a , "\nTime : " , ticker.time , "\nBid : " , ticker.bid ,"\nAsk : "  , ticker.ask ,"\nbidSize : "  , ticker.bidSize ,"\naskSize : "  , ticker.askSize ,"\nPrice : " , ticker.ticks[0].price)
print("#############################################")

# a = Forex('JPYUSD')
# ib.reqMktData(a, '', False, False)
# ticker = ib.ticker(a)
# ib.sleep(20)
# print("\n\n\n")
# print(ticker)
# print("\n\n\n")
# print("\nForex : " , a , "\nTime : " , ticker.time , "\nBid : " , ticker.bid ,"\nAsk : "  , ticker.ask ,"\nbidSize : "  , ticker.bidSize ,"\naskSize : "  , ticker.askSize ,"\nPrice : " , ticker.ticks[0].price)
# print("#############################################")

# a = Stock('AMD', 'SMART', 'USD')
# ib.reqMktData(a, '', False, False)
# ticker = ib.ticker(a)
# ib.sleep(10)
# print("\n\n\n")

# print("\n\n\n")

# print("\nForex : " , a , "\nTime : " , ticker.time , "\nBid : " , ticker.bid ,"\nAsk : "  , ticker.ask ,"\nbidSize : "  , ticker.bidSize ,"\naskSize : "  , ticker.askSize ,"\nPrice : " , ticker.ticks[0].price)
# print("#############################################")

# a = Future('ES', '20180921', 'GLOBEX')
# ib.reqMktData(a, '', False, False)
# ticker = ib.ticker(a)
# ib.sleep(10)
# print("\n\n\n")

# print("\n\n\n")

# print("\nForex : " , a , "\nTime : " , ticker.time , "\nBid : " , ticker.bid ,"\nAsk : "  , ticker.ask ,"\nbidSize : "  , ticker.bidSize ,"\naskSize : "  , ticker.askSize ,"\nPrice : ")
# print("#############################################")

# a = Option('SPY', '20170721', 240, 'C', 'SMART') 
# ib.reqMktData(a, '', False, False)
# ticker = ib.ticker(a)
# ib.sleep(10)
# print("\n\n\n")

# print("\n\n\n")

# print("\nForex : " , a , "\nTime : " , ticker.time , "\nBid : " , ticker.bid ,"\nAsk : "  , ticker.ask ,"\nbidSize : "  , ticker.bidSize ,"\naskSize : "  , ticker.askSize ,"\nPrice : " , ticker.ticks[0].price)
# print("#############################################")

# a = Bond(secIdType='ISIN', secId='US03076KAA60')
# ib.reqMktData(a, '', False, False)
# ticker = ib.ticker(a)
# ib.sleep(10)
# print("\n\n\n")

# print("\n\n\n")

# print("\nForex : " , a , "\nTime : " , ticker.time , "\nBid : " , ticker.bid ,"\nAsk : "  , ticker.ask ,"\nbidSize : "  , ticker.bidSize ,"\naskSize : "  , ticker.askSize ,"\nPrice : " , ticker.ticks[0].price)
# print("#############################################")

# a = Stock('INTC', 'SMART', 'USD', primaryExchange='NASDAQ')
# ib.reqMktData(a, '', False, False)
# ticker = ib.ticker(a)
# ib.sleep(10)
# print("\n\n\n")

# print("\n\n\n")
# print("\nForex : " , a , "\nTime : " , ticker.time , "\nBid : " , ticker.bid ,"\nAsk : "  , ticker.ask ,"\nbidSize : "  , ticker.bidSize ,"\naskSize : "  , ticker.askSize ,"\nPrice : " , ticker.ticks[0].price)
# print("#############################################")