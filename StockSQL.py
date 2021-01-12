#!/usr/bin/env python3

print("StockTracker, built by Adrian")
print("Importing yfinance")
import yfinance
print("Importing mysql")
import mysql.connector
from mysql.connector import errorcode
from mysql.connector import (connection)
print("Importing time")
import datetime

print("Connecting to mySQL server")
try:
  mydb = mysql.connector.connect(
    user='adrian',
    password = '[redacted]',
    host = 'localhost',
    database = 'mydatabase')
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your username or password!")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
  
cursor = mydb.cursor()

print("Connected to mySQL server")

end = False
print("Started! For help, type help. To end, type end\n")

while end == False:
  inputCommand = input()

  # help command
  if(inputCommand == "help"):
    print("List of Commands")
    print("help - list of commands and descriptions")
    print("addStock - adds a stock from tracking")
    print("deleteStock - deletes a stock from tracking")
    print("updateStock - refreshes the stock prices from the Yahoo Finance API")
    print("checkStats - checks the various statistics of the portfolio")
    print("end - ends the program")
  
  # Adds a stock to tracking in the mySQL Database. Also verifies it exists. 
  elif(inputCommand == "addStock"):
    print("What is the ticker?")
    ticker = str(input())
    print("How long are you expecting to hold?(Short/Mid/Long)")
    holdLength = str(input())
    print("How many shares have been bought?")
    sharesBought = float(input())
    print("What day did you buy them?(YYYY-MM-DD)")
    dateBought = str(input())
    print("What price did you buy them at?")
    price = float(input())
    print("Checking the stock on the yahoo finance API")
    stockTicker = yfinance.Ticker(ticker)
    print("Stock found! Creating mySQL entry")
    stockInfo = stockTicker.info
    stockName = stockInfo['longName']
    
    dateformat = "%Y-%m-%d"
    now = datetime.datetime.strptime(dateBought,dateformat)
    now.strftime(dateformat)

    sql = "INSERT INTO Stocks(StockName, Ticker, HoldLength, PriceBought, SharesBought, DateBought) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (stockName, ticker, holdLength, price, sharesBought, now)
    cursor.execute(sql, val)
    mydb.commit()
    cost = "{:.2f}".format(sharesBought*price)
    print(cost + " dollars of stock from " + stockName + " successfully added!")
  
  # deletes a stock from tracking
  elif(inputCommand == "deleteStock"):
    print("What is the stock ticker of the stock being deleted?")
    stock = str(input())
    stockTicker = yfinance.Ticker(stock)
    stockInfo = stockTicker.info
    stockName = stockInfo['longName']
    print("Deleting " + stockName)
    sql = "DELETE FROM Stocks WHERE Ticker = %s"
    val = (stock,)
    cursor.execute(sql,val)
    mydb.commit()
    print("Stock " + stockName + " removed from the database")

  # update stock command
  elif(inputCommand == "updateStock"):
    print("Do you want to update a specific stock or all?")
    inputString = input()
    if(inputString == "all"):
      
    else:
      

  # check statistics command
  elif(inputCommand == "checkStats"):
    print("Check all or specific?")
    inputCommand = input()
    if(inputCommand == "all"):
      print("To be implemented")
    else:
      print("To be implemented")

  # ends the program
  elif(inputCommand == "end"):
    print("Ending session")
    cursor.close()
    mydb.close()
    end = True

  # catches invalid queries
  else:
    print("Not a command!")
  print()
