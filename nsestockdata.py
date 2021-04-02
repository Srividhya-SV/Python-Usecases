from nsetools import Nse
from prettytable import PrettyTable
import sys

#Function to retrieve the NSE stock data
def getstockdata(stocklist):
    nse = Nse()
    # Creating Prettytable to display the stock data in user readable format
    t = PrettyTable(['Stock_Name', 'Open', 'High', 'Low', 'Close', 'Volume', 'Delivery Data', 'Delivery Percentage'])

    #Iterating the list of stocks to retrieve the stock data
    for stock in stocklist:
        #Iterating each stock
        stock_data = nse.get_quote(stock)
        #Adding stock_data to the table
        t.add_row([stock_data['symbol'], stock_data['open'], stock_data['dayHigh'], stock_data['dayLow'], stock_data['closePrice'],
                   stock_data['deliveryToTradedQuantity'], stock_data['totalBuyQuantity'], stock_data['pChange']])

    return t

n = len(sys.argv[1])
stock_list = sys.argv[1][1:n - 1]
stock_list = stock_list.split(',')

#Function call to fetch the stock data
output_table = stock_data = getstockdata(stock_list)

print(output_table)
