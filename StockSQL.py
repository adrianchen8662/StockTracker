#!/usr/bin/env python3

print("StockTracker, built by Adrian")
print("Importing yfinance")
import yfinance
print("Importing mysql")
import mysql.connector

mydb = mysql.connector.connect(
  host = "localhost",
  user = "adrian",
  password = "HaoRan8662@",
  database = "mydatabase"
)
mycursor = mydb.cursor()
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
    print("How long are you expecting to hold?(Short/Long)")
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

    sql = "INSERT INTO Stocks(StockName, Ticker, HoldLength, PriceBought, SharesBought, DateBought) VALUES (%s %s %s %f %f %s)"
    val = (stockName, ticker, holdLength, price, sharesBought, dateBought)
    cost = "{:.2f}".format(sharesBought*price)
    print(cost + " dollars of stock from " + stockName + " successfully added!")
  
  # deletes a stock from tracking
  elif(inputCommand == "deleteStock"):
    print("To be implemented")

  # update stock command
  elif(inputCommand == "updateStock"):
    print("To be implemented")

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
    end = True

  # catches invalid queries
  else:
    print("Not a command!")
  print()
