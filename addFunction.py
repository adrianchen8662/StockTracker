#!/usr/bin/env python3

import mysql.connector
import time
import yfinance as yf

def addStock():
  print("What's the ticker?")
  ticker = input()
  print("How long are you expecting to hold?(Short/Long)")
  holdLength = input()
  print("How many shares have been bought?")
  sharesBought = input()
  print("What day did you buy them?(YYYY-MM-DD)")
  dateBought = input()
  print("What price did you buy them at?")
  price = input()
  
  mydb = mysql.connector.connect(
    host = "localhost",
    user = "adrian",
    password = "HaoRan8662@",
    database = "mydatabase"
  )

  mycursor = mydb.cursor()

  print("Checking on yahoo finance API")
  #yep = yf.Ticker(ticker)
  yep = yf.Ticker("GOOG")
  tickerinfo = yep.info # problem is here
  StockName = tickerinfo['longName']

  print("Creating mySQL entry")
  sql = "INSERT INTO Stocks (StockName, Ticker, HoldLength, PriceBought, SharesBought, DateBought) VALUES (%s %s %s %f %f %f)"
  val = (StockName, ticker, holdLength, price, sharesBought, dateBought)
  StockSQL.mycursor.execute(sql,val)
  StockSQL.mydb.commit()

  print("Stock " + StockName + " successfully added!")
