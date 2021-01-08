#!/user/bin/env python3

def help Function():
  print("List of Commands\n")
  print("addStokc - adds a stock from tracking\n")
  print(" * Fields: addStock(Ticker, HoldLength, SharesBought)\n")
  print("deleteStock - deletes a stock from tracking\n");
  print(" * Fields: deleteStock(Ticker)\n")
  print("updateStock - refreshes the stock listings from the Yahoo Finance API\n")
  print("checkStats - checks the various statistics of the portfolio\n")
