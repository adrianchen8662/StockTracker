#!/usr/bin/env python3

import StockSQLHelp.py
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
