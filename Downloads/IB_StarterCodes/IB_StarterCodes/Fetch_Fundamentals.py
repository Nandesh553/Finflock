from ib_insync import *
import pandas as pd
import os
import sys

ib = IB()
ib.connect('127.0.0.1', 4002, clientId=9898)

# a = Stock('IBM', 'NYSE', 'USD', primaryExchange='NYSE')
# Stock_List = ['AAPL' , 'IBM' , 'GOOG']
# for i in Stock_List:
#     contract = Contract()
#     contract.symbol = i
#     contract.secType = "STK"
#     contract.currency = "USD"
#     contract.exchange = "SMART"
#     contract.primaryExchange = "SMART"


Stock_List = ['TATAMOTOR' , 'TCS' , 'RELIANCE']
for i in Stock_List:
    contract = Contract()
    contract.symbol = i
    contract.secType = "STK"
    contract.currency = "INR"
    contract.exchange = "NSE"
    contract.primaryExchange = "NSE"

    try:
        print("Fetching ReportsFinSummary..")
        ticker = ib.reqFundamentalData( contract,"ReportsFinSummary", [])
        filename = str(i)+"_Fundamental_Data/"+str(i) + "_ReportsFinSummary.xml"
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        t = open(filename, 'w')
        t.write(ticker)
        t.close()

    except:
        print("ERROR")


    try:
        print("Fetching ReportsOwnership..")
        ticker = ib.reqFundamentalData( contract,"ReportsOwnership", [])
        filename = str(i)+"_Fundamental_Data/"+str(i) + "_ReportsOwnership.xml"
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        t = open(filename, 'w')
        t.write(ticker)
        t.close()
    except:
        print("ERROR")

    try:
        print("Fetching ReportSnapshot..")
        ticker = ib.reqFundamentalData( contract,"ReportSnapshot", [])
        filename = str(i)+"_Fundamental_Data/"+str(i) + "_ReportSnapshot.xml"
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        t = open(filename , 'w')
        t.write(ticker)
        t.close()
    except:
        print("ERROR")

    try:
        print("Fetching ReportsFinStatements..")
        ticker = ib.reqFundamentalData( contract,"ReportsFinStatements", [])
        filename = str(i)+"_Fundamental_Data/"+str(i) + "_ReportsFinStatements.xml"
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        t = open(filename , 'w')
        t.write(ticker)
        t.close()
    except:
        print("ERROR")

    try:
        print("Fetching RESC..")
        ticker = ib.reqFundamentalData( contract,"RESC", [])
        filename = str(i)+"_Fundamental_Data/"+str(i) + "_RESC.xml"
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        t = open(filename , 'w')
        t.write(ticker)
        t.close()

    except:
        print("ERROR")