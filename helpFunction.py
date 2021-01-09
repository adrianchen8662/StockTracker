#!/user/bin/env python3

def helpFunction():
  print("List of Commands")
  print("addStock - adds a stock from tracking")
  print(" * Fields: addStock(Ticker, HoldLength, SharesBought)")
  print("deleteStock - deletes a stock from tracking");
  print(" * Fields: deleteStock(Ticker)")
  print("updateStock - refreshes the stock listings from the Yahoo Finance API")
  print("checkStats - checks the various statistics of the portfolio")
  print(" * Fields: checkStats(Ticker) or checkStats(all)")
