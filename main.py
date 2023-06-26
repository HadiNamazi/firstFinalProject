from datetime import datetime
import pandas as pd
import plotly.express as px

# Csv: comma separated values
# for pandas copy error
pd.options.mode.chained_assignment = None



class Stocks:
    # A method with which we calculate the percentage of the change of stock values throughout the years
    def show_chgpercent(self):
        df = pd.read_csv(r'./stock_market_data.csv')
        amzn_q = "Symbol == 'AMZN'"
        fb_q = "Symbol == 'FB'"
        tsla_q = "Symbol == 'TSLA'"
        googl_q = "Symbol == 'GOOGL'"
        aapl_q = "Symbol == 'AAPL'"
        amzn = df.query(amzn_q)
        fb = df.query(fb_q)
        tsla = df.query(tsla_q)
        googl = df.query(googl_q)
        aapl = df.query(aapl_q)

        #Calculating the first and last price of each stock
        first_amzn = amzn['Open'][amzn['Open'].axes[0][0]]
        last_amzn = amzn['Open'][amzn['Open'].size - 1 + amzn['Open'].axes[0][0]]
        first_fb = fb['Open'][fb['Open'].axes[0][0]]
        last_fb = fb['Open'][fb['Open'].size - 1 + fb['Open'].axes[0][0]]
        first_tsla = tsla['Open'][tsla['Open'].axes[0][0]]
        last_tsla = tsla['Open'][tsla['Open'].size - 1 + tsla['Open'].axes[0][0]]
        first_googl = googl['Open'][googl['Open'].axes[0][0]]
        last_googl = googl['Open'][googl['Open'].size - 1 + googl['Open'].axes[0][0]]
        first_aapl = aapl['Open'][aapl['Open'].axes[0][0]]
        last_aapl = aapl['Open'][aapl['Open'].size - 1 + aapl['Open'].axes[0][0]]

        #Calculating the percentage
        chgp_dict = {'AMZN': ((last_amzn-first_amzn)/first_amzn)*100,
                     'FB': ((last_fb-first_fb)/first_fb)*100,
                     'TSLA': ((last_tsla-first_tsla)/first_tsla)*100,
                     'GOOGL': ((last_googl-first_googl)/first_googl)*100,
                     'AAPL': ((last_aapl-first_aapl)/first_aapl)*100 }
        # Sortign the dictionary in descending order // reverse = True
        chgp_dict = sorted(chgp_dict.items(), key=lambda item: item[1])

        #printing the results
        i = 4
        while i >= 0:
            print(chgp_dict[i][0], chgp_dict[i][1], '%')
            i -= 1

    # A method that shows the linear regression chart of the given stock
    def show_reg_chart(self, stock):
        df = pd.read_csv(r'./stock_market_data.csv')
        query = "Symbol == '" + stock + "'"
        selected_stock = df.query(query)
        #selected_stock['Volume'].axes[0][0] aka the 0th index of the given stock
        for i in range(selected_stock['Volume'].axes[0][0], selected_stock['Volume'].size + selected_stock['Volume'].axes[0][0]):
            #time_data is the time present in string format
            #format_data is the data present in datetime format which is converted from time_data using this function.
            selected_stock['Date'][i] = datetime.strptime(str(time_data= selected_stock['Date'][i]), format_data= '%Y-%m-%d')
        # Determinig the x and y of the chart // ols :linear 
        #Array-like and dict are transformed internally to a pandas DataFrame. 
        #Optional: if missing, a DataFrame gets constructed under the hood using the other arguments.
        fig = px.scatter(data_frame= selected_stock, x='Date', y='Open', trendline="ols", trendline_color_override='red')
        # linkes to a page in which the chart is depicted
        fig.show()

    # A method that shows the chart of the given stock
    def show_chart(self, stock):
        df = pd.read_csv(r'./stock_market_data.csv')
        query = "Symbol == '" + stock + "'"
        selected_stock = df.query(query)
        #Array-like and dict are transformed internally to a pandas DataFrame. 
        #Optional: if missing, a DataFrame gets constructed under the hood using the other arguments.
        fig = px.line(data_frame= selected_stock, x='Date', y='Open')
        fig.show()

#The unlucky owner of the account
class Account:
    firstname = ''
    lastname = ''
    mellicode = 0
    birthday = ''
    asset = 0
    stocks = []

    # A method that buys the given stock and reduces our asset by the value of the given stock
    def buy_stock(self, stock, n):
        df = pd.read_csv(r'./stock_market_data.csv')
        # Pandas query() acts as a data frame filter
        query = "Symbol == '" + stock + "'"
        selected_stock = df.query(query)
        # The latest price of the given stock
        price = selected_stock['Open'][selected_stock['Symbol'].axes[0][0] + selected_stock['Symbol'].size  - 1]
        if self.asset >= price*n:
            for i in range(0, n):
                self.stocks.append(stock)
            self.asset -= price*n
            print('The purchase of {} shares was successfully completed.'.format(stock))
        else:
            print('Unfortunately you do not have enough asset to buy this stock.')

    # A method that sells the given stock and adds the value of the given stock to our asset
    def sell_stock(self, stock, n):
        if stock in self.stocks:
            df = pd.read_csv(r'./stock_market_data.csv')
            query = "Symbol == '" + stock + "'"
            selected_stock = df.query(query)
            # The latest price of the given stock
            price = selected_stock['Open'][selected_stock['Open'].size - 1 + selected_stock['Open'].axes[0][0]]
            self.asset += price*n
            for i in range(0, n):
                self.stocks.remove(stock)
            print('The sale of {} shares has been successfully completed.'.format(stock))
        else:
            print('Unfortunately you do not have this stock in your account')

    # A method that prints our stocks and the total value of them
    def show_stocks(self):
        df = pd.read_csv(r'./stock_market_data.csv')
        # q stands for query
        amzn_q = "Symbol == 'AMZN'"
        fb_q = "Symbol == 'FB'"
        tsla_q = "Symbol == 'TSLA'"
        googl_q = "Symbol == 'GOOGL'"
        aapl_q = "Symbol == 'AAPL'"
        amzn = df.query(amzn_q)
        fb = df.query(fb_q)
        tsla = df.query(tsla_q)
        googl = df.query(googl_q)
        aapl = df.query(aapl_q)

        #In this sections we calculate the total value of our stock(well....it turns out it's just virtual money)
        value = 0
        for i in range(0, len(self.stocks)):
            if self.stocks[i] == 'AMZN':
                value += amzn['Open'][amzn['Open'].size + amzn['Open'].axes[0][0] - 1]
            elif self.stocks[i] == 'FB':
                value += fb['Open'][fb['Open'].size + fb['Open'].axes[0][0] - 1]
            elif self.stocks[i] == 'TSLA':
                value += tsla['Open'][tsla['Open'].size + tsla['Open'].axes[0][0] - 1]
            elif self.stocks[i] == 'GOOGL':
                value += googl['Open'][googl['Open'].size + googl['Open'].axes[0][0] - 1]
            elif self.stocks[i] == 'AAPL':
                value += aapl['Open'][aapl['Open'].size + aapl['Open'].axes[0][0] - 1]

        print('Your stocks:', self.stocks, '\n', 'Total value of your stocks:', '\t', value,'$')

