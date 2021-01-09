#!/usr/bin/env python3

print("StockTracker, built by Adrian")
print("Importing functions")
import helpFunction
print("Importing mysql connector")
import mysql.connector
print("Importing Yahoo Finance API")
from yahoo_finance import Share

print("Connecting to mySQL")
mydb = mysql.connector.connect(
  host="localhost",
  user="adrian",
  password="HaoRan8662@",
  database="mydatabase"
)
end = False
mycursor = mydb.cursor()

print("Started! For help, type help. To end, type end\n")
while end == False:
  inputCommand = input();
  if(inputCommand == "help"):
    helpFunction.helpFunction()
  elif(inputCommand == "addStock"):
    print("To be implemented")
    #addStock()
  elif(inputCommand == "deleteStock"):
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
