#Super Simple Stock Market

import time
import math

class Stock(object):
    
   #Constructor    
   def __init__(self, stockSymbol, stockType, lastDividend, fixedDividend=None, parValue=100):
        self.stockSymbol = stockSymbol
        self.stockType = stockType
        self.lastDividend = lastDividend
        self.fixedDividend = fixedDividend
        self.parValue = parValue
        self.trades = []

class StockExchange(object):
    
    #Constructor
    def __init__(self):
        self.stocks = {}
        self.timestamps = {}
        self.geometricMean = None

    def addStock(self, stock):
        self.stocks[stock. stockSymbol] = stock
        self.timestamps[stock.stockSymbol] = []

    def calculateDividendYield(self, stockSymbol, price):
        stock = self.stocks.get(stockSymbol)
        if stock:
            if stock.stockType == "Common":
                return stock.lastDividend / price
            elif stock.stockType == "Preferred" and stock.fixedDividend is not None:
                return (stock.fixedDividend * stock.parValue) / price
        return None

    def calculatePeRatio(self, stockSymbol, price):
        stock = self.stocks.get(stockSymbol)
        if stock and stock.lastDividend > 0:
            return price / stock.lastDividend
        return None

    def recordTrade(self, stockSymbol, quantity, buySellIndicator, price):
        stock = self.stocks.get(stockSymbol)
        if stock:
            timestamp = time.time()
            self.timestamps[stockSymbol].append(timestamp)
            stock.trades.append((timestamp, quantity, buySellIndicator, price))

    def calculateVolumeWeightedStockPrice(self, stockSymbol):
        stock = self.stocks.get(stockSymbol)
        if stock:
            fifteenMinutesAgo = time.time() - 15 * 60  
            recentTrades = [trade for trade in stock.trades if trade[0] >= fifteenMinutesAgo]
            if recentTrades:
                totalPriceQuantity = sum(trade[1] * trade[3] for trade in recentTrades)
                totalQuantity = sum(trade[1] for trade in recentTrades)
                return totalPriceQuantity / totalQuantity
        return None

    def calculateGeometricMean(self):
        prices = {}
        for stockSymbol in self.stocks:
            stock = self.stocks[stockSymbol]
            if stock.trades:
                prices[stockSymbol] = stock.trades[-1][3]  # Last trade price
        if prices:
            self.geometricMean = math.prod(prices.values())**(1/len(prices))

if __name__ == "__main__":
    # to create stock objects with the provided data in the assignment
    tea = Stock("TEA", "Common", 0)
    pop = Stock("POP", "Common", 8)
    ale = Stock("ALE", "Common", 23)
    gin = Stock("GIN", "Preferred", 8, 0.02)
    joe = Stock("JOE", "Common", 13)

    # to create the stock exchange and add stocks
    exchange = StockExchange()
    exchange.addStock(tea)
    exchange.addStock(pop)
    exchange.addStock(ale)
    exchange.addStock(gin)
    exchange.addStock(joe)

    # Eg:
    price = 100  
    stockSymbol = "TEA"  
    dividendYield = exchange.calculateDividendYield(stockSymbol, price)
    peRatio = exchange.calculatePeRatio(stockSymbol, price)
    print(f"Dividend Yield for {stockSymbol} is {dividendYield}")
    print(f"P/E Ratio for { stockSymbol } is {peRatio}")
    # Record a trade
    exchange.recordTrade(stockSymbol, quantity=10, buySellIndicator="Buy", price=price)
    # to calculate Volume Weighted Stock Price
    vwsp = exchange.calculateVolumeWeightedStockPrice(stockSymbol)
    print(f"Volume Weighted Stock Price for is {stockSymbol}: {vwsp}")
    #to calculate GBCE All Share Index
    exchange.calculateGeometricMean()
    print(f"GBCE All Share Index is {exchange.geometricMean}")

