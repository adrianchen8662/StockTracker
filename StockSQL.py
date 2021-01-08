#!/usr/bin/env python3

import mysql.connector
from yahoo_finance import Share

#Main Function
mydb = mysql.connector.connect(
  host="localhost",
  user="adrian",
  password="HaoRan8662@",
  database="mydatabase"
)

mycursor = mydb.cursor()

while end=false:
  inputCommand = input();
  if(inputCommand = "help"):
    helpFunction()
  else if(inputcommand = "addStock"):
    addStock()
  else if(inputcommand = "deleteStock"):
    deleteStock()
  else if(inputcommand = "updateStock"):
    updateStock()
  else if(inputcommand = "checkStats"):
    checkStats()
  else
    print("Command not recognized!");

#help Function
def helpFunction():
  print("List of Commands\n")
  print("addStock - adds a stock from tracking.\n")
  print("* Fields: addStock(Ticker, HoldLength, SharesBought)\n")
  print("deleteStock - deletes a stock from tracking. \n")
  print("* Fields: deleteStock(Ticker)\n")
  print("updateStock - refreshes the stock listings from the Yahoo Finance API\n")
  print("checkStats - checks the various statistics of the portfolio\n")

#addStock Function
def addStock():
  

#deleteStock Function
def deleteStock():
  

#updateStock Function
def updateStock():


#checkStats Function
def checkStats():
  
