import requests

class StockPortfolio:
    def __init__(self, api_key):
        """
        Initialize the portfolio with an API key for Alpha Vantage.
        """
        self.api_key = api_key
        self.portfolio = {}

    def add_stock(self, ticker, shares, purchase_price):
        """
        Add stock to the portfolio. If the stock is already in the portfolio,
        add the new shares to the existing position and update the average purchase price.
        """
        if ticker in self.portfolio:
            existing_shares = self.portfolio[ticker]['shares']
            total_spent = self.portfolio[ticker]['purchase_price'] * existing_shares
            new_total_spent = total_spent + purchase_price * shares
            new_total_shares = existing_shares + shares
            new_avg_price = new_total_spent / new_total_shares
            self.portfolio[ticker] = {'shares': new_total_shares, 'purchase_price': new_avg_price}
            print(f"Updated {ticker}: {new_total_shares} shares at an average price of ${new_avg_price:.2f}.")
        else:
            self.portfolio[ticker] = {'shares': shares, 'purchase_price': purchase_price}
            print(f"Added {ticker}: {shares} shares at ${purchase_price:.2f} per share.")

    def remove_stock(self, ticker):
        """Remove stock from the portfolio."""
        if ticker in self.portfolio:
            del self.portfolio[ticker]
            print(f"Removed {ticker} from portfolio.")
        else:
            print(f"{ticker} is not in the portfolio.")

    def get_stock_price(self, ticker):
        """
        Fetch the current stock price using Alpha Vantage API.
        Returns the closing price of the stock.
        """
        url = f"https://www.alphavantage.co/query"
        params = {
            "function": "TIME_SERIES_INTRADAY",
            "symbol": ticker,
            "interval": "1min",
            "apikey": self.api_key
        }
        response = requests.get(url, params=params)
        data = response.json()
        
        if 'Time Series (1min)' in data:
            latest_time = list(data['Time Series (1min)'].keys())[0]
            current_price = float(data['Time Series (1min)'][latest_time]['4. close'])
            return current_price
        else:
            print(f"Error fetching data for {ticker}: {data.get('Error Message', 'Unknown error')}")
            return None

    def calculate_portfolio_value(self):
        """Calculate the total current value of the portfolio."""
        total_value = 0
        for ticker, data in self.portfolio.items():
            current_price = self.get_stock_price(ticker)
            if current_price is not None:
                total_value += current_price * data['shares']
        return total_value

    def calculate_performance(self):
        """Calculate and display the performance of the portfolio."""
        total_invested = 0
        total_value = 0
        for ticker, data in self.portfolio.items():
            current_price = self.get_stock_price(ticker)
            if current_price is not None:
                invested = data['purchase_price'] * data['shares']
                total_invested += invested
                total_value += current_price * data['shares']
                print(f"{ticker}: {data['shares']} shares, bought at ${data['purchase_price']:.2f}, current price: ${current_price:.2f}, value: ${current_price * data['shares']:.2f}")
        
        print(f"\nTotal invested: ${total_invested:.2f}")
        print(f"Current portfolio value: ${total_value:.2f}")
        print(f"Portfolio performance: ${total_value - total_invested:.2f} (Gain/Loss)")


# Example usage
if __name__ == "__main__":
    # Replace with your actual Alpha Vantage API key
    api_key = "your_alpha_vantage_api_key"
    portfolio = StockPortfolio(api_key)

    # Adding stocks
    portfolio.add_stock('AAPL', 10, 150)  # 10 shares of Apple at $150
    portfolio.add_stock('GOOG', 5, 1000)  # 5 shares of Google at $1000
    portfolio.add_stock('AAPL', 5, 160)   # Another 5 shares of Apple at $160 (updating average)

    # Display portfolio performance
    portfolio.calculate_performance()

    # Removing a stock
    portfolio.remove_stock('AAPL')

    # Display performance after removing a stock
    portfolio.calculate_performance()
