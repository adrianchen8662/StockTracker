# StockTracker

Python and mySQL project to create an automatic stock tracker that updates using the yahoo finance API. Created out of a need for better/cleaner statistics than what Robinhood provides. 

Features:
Add a stock, delete a stock, manual update from the API, automatic update from the API, and a statspage that tracks various things that I care about. 

mySQL List Entries:
StockName varchar(100) - name of the stock
Ticker varchar(10) - ticker of the stock
HoldLength varchar(5) - time for speculation(short/long)
PriceBought decimal(5,2) - price per share that it was bought at
SharesBought decimal(6,6) - amount of shares bought(partial included)
DateBought date - date bought

Statspage all features: 
- [ ] Performance today, money and percentage, delta percentage compared to nasdaq and s&p 500
- [ ] Performance this week, money and percentage, delta percentage compared to nasdaq and s&p 500
- [ ] Performance this month, money and percentage, delta percentage compared to nasdaq and s&p 500
- [ ] Performance this year, money and percentage, delta percentage compared to nasdaq and s&p 500
- [ ] Performance year-to-date, money and percentage, delta percentage compared to nasdaq and s&p 500
- [ ] Performance since start, money and percentage, delta percentage compared to nasdaq and s&p 500
- [ ] Percentage holding of each stock

Statspage seperate features: 
All of the above, but separate

Todo:
- [X] Help/Commandpage function
- [ ] Add stock function
- [ ] Delete stock function
- [ ] Manual update stock function
- [ ] Automatic update stock function
- [ ] Statistics function - all and individual
- [ ] Yahoo Finance API integration
- [ ] mySQL Creation/Integration

Stretch goals:  
- [ ] Options
- [ ] GUI
- [ ] Historical Data/Graphs, maybe interactive
- [ ] Stock price alerts
