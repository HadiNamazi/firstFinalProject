from datetime import datetime
import pandas as pd
import plotly.express as px

# for pandas copy error
pd.options.mode.chained_assignment = None



class Stocks:
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

        chgp_dict = {'AMZN': ((last_amzn-first_amzn)/first_amzn)*100,
                     'FB': ((last_fb-first_fb)/first_fb)*100,
                     'TSLA': ((last_tsla-first_tsla)/first_tsla)*100,
                     'GOOGL': ((last_googl-first_googl)/first_googl)*100,
                     'AAPL': ((last_aapl-first_aapl)/first_aapl)*100 }

        chgp_dict = sorted(chgp_dict.items(), key=lambda item: item[1])

        i = 4
        while i >= 0:
            print(chgp_dict[i][0], chgp_dict[i][1], '%')
            i -= 1

    def show_reg_chart(self, stock):
        df = pd.read_csv(r'./stock_market_data.csv')
        query = "Symbol == '" + stock + "'"
        selected_stock = df.query(query)
        for i in range(selected_stock['Volume'].axes[0][0], selected_stock['Volume'].size + selected_stock['Volume'].axes[0][0]):
            selected_stock['Date'][i] = datetime.strptime(str(selected_stock['Date'][i]), '%Y-%m-%d')
        fig = px.scatter(selected_stock, x='Date', y='Open', trendline="ols", trendline_color_override='red')
        fig.show()

    def show_chart(self, stock):
        df = pd.read_csv(r'./stock_market_data.csv')
        query = "Symbol == '" + stock + "'"
        selected_stock = df.query(query)
        fig = px.line(data_frame=selected_stock, x='Date', y='Open')
        fig.show()

class Account:
    firstname = ''
    lastname = ''
    mellicode = 0
    birthday = ''
    asset = 0
    stocks = []

    def buy_stock(self, stock):
        df = pd.read_csv(r'./stock_market_data.csv')
        query = "Symbol == '" + stock + "'"
        selected_stock = df.query(query)
        price = selected_stock['Open'][selected_stock['Symbol'].axes[0][0]]
        if self.asset >= price:
            self.stocks.append(stock)
            self.asset -= price
            print('The purchase of {} shares was successfully completed'.format(stock))
        else:
            print('unfortunately you have not enough asset to buy this stock')


    def sell_stock(self, stock):
        if stock in self.stocks:
            df = pd.read_csv(r'./stock_market_data.csv')
            query = "Symbol == '" + stock + "'"
            selected_stock = df.query(query)
            price = selected_stock['Open'][selected_stock['Open'].size - 1 + selected_stock['Open'].axes[0][0]]
            self.asset += price
            self.stocks.remove(stock)
            print('The sale of Amazon shares has been successfully completed')
        else:
            print('unfortunately you have not this stock in your account')


    def show_stocks(self):
        df = pd.read_csv(r'./stock_market_data.csv')
        # amazon query
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
        
        price = 0
        for i in range(0, len(self.stocks)):
            if self.stocks[i] == 'AMZN':
                price += amzn['Open'][amzn['Open'].size + amzn['Open'].axes[0][0] - 1]
            elif self.stocks[i] == 'FB':
                price += fb['Open'][fb['Open'].size + fb['Open'].axes[0][0] - 1]
            elif self.stocks[i] == 'TSLA':
                price += tsla['Open'][tsla['Open'].size + tsla['Open'].axes[0][0] - 1]
            elif self.stocks[i] == 'GOOGL':
                price += googl['Open'][googl['Open'].size + googl['Open'].axes[0][0] - 1]
            elif self.stocks[i] == 'AAPL':
                price += aapl['Open'][aapl['Open'].size + aapl['Open'].axes[0][0] - 1]

        print('Your stocks:', self.stocks, '\n', 'Total value of your stocks:', '\t', price,'$')

