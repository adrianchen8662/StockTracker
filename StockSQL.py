#!/usr/bin/env python3

print("StockTracker, built by Adrian")
print("Importing functions")
import helpFunction
import addFunction
import checkFunction
import deleteFunction
import updateFunction
print("Importing Yahoo Finance API")
import yfinance as yf
#import mysql

end = False

print("Started! For help, type help. To end, type end\n")
while end == False:
  inputCommand = input();
  if(inputCommand == "help"):
    helpFunction.helpFunction()
  elif(inputCommand == "addStock"):
    print("What is the ticker?")
    ticker = input()
    print("How long are you expecting to hold?(Short/Long)")
    holdLength = input()
    print("How many shares have been bought?")
    sharesBought = input()
    print("What day did you buy them?(YYYY-MM-DD)")
    dateBought = input()
    print("What price did you buy them at?")
    price = input()
  
#    mydb = mysql.connector.connect(
#      host = "localhost",
#      user = "adrian",
#      password = "HaoRan8662@",
#      database = "mydatabase"
#    )

#    mycursor = mydb.cursor()

    print("Checking on yahoo finance API")
    #yep = yf.Ticker(ticker)
    yep = yf.Ticker("GOOG")
    tickerinfo = yep.info # problem is here
    StockName = tickerinfo['longName']

#    print("Creating mySQL entry")
#    sql = "INSERT INTO Stocks (StockName, Ticker, HoldLength, PriceBought, SharesBought, DateBought) VALUES (%s %s %s %f %f %f)"
#    val = (StockName, ticker, holdLength, price, sharesBought, dateBought)
#    StockSQL.mycursor.execute(sql,val)
#    StockSQL.mydb.commit()

    print("Stock " + StockName + " successfully added!")
 # elif(inputCommand == "deleteStock"):
    print("To be implemented")
    #deleteStock()
  elif(inputCommand == "updateStock"):
    print("To be implemented")
    #updateStock()
  elif(inputCommand == "checkStats"):
    print("To be implemented")
    #checkStats()
  elif(inputCommand == "end"):
    print("Shutting down")
    end = True
  else:
    print("Command not recognized!");
  print()
