from datetime import datetime

class Trade:
    """
    Represents a single trade record (buy or sell).
    Demonstrates Encapsulation (private attributes) and Magic Methods.
    """
    def __init__(self, ticker: str, action: str, price: float, quantity: int, date: str):
        self.__ticker = ticker
        self.__action = action.upper()
        self.__price = price
        self.__quantity = quantity
        self.__date = self.__parse_date(date)

    @property
    def ticker(self) -> str:
        return self.__ticker

    @property
    def action(self) -> str:
        return self.__action

    @property
    def quantity(self) -> int:
        return self.__quantity

    @property
    def total_value(self) -> float:
        return self.__price * self.__quantity

    @property
    def date(self) -> datetime:
        return self.__date
        
    @staticmethod
    def __parse_date(date_str: str) -> datetime:
        # Static method to handle date parsing formats
        try:
            return datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            return datetime.now() # Fallback

    def __str__(self) -> str:
        # Magic method for string representation
        return f"{self.__date.strftime('%Y-%m-%d')} | {self.__action} {self.__quantity} shares of {self.__ticker} at ${self.__price:.2f}"

class StockPosition:
    """
    Manages the cumulative position and profit for a specific stock ticker.
    """
    def __init__(self, ticker: str):
        self.ticker = ticker
        self.__total_shares = 0
        self.__total_cost = 0.0
        self.__realized_profit = 0.0

    def add_trade(self, trade: Trade):
        if trade.action == "BUY":
            self.__total_shares += trade.quantity 
            self.__total_cost += trade.total_value
        elif trade.action == "SELL":
            # Simplified average cost calculation
            if self.__total_shares > 0:
                avg_cost = self.__total_cost / self.__total_shares
                self.__realized_profit += trade.total_value - (avg_cost * trade.quantity)
                self.__total_shares -= trade.quantity
                self.__total_cost -= avg_cost * trade.quantity

    @property
    def profit(self) -> float:
        return self.__realized_profit

    def __str__(self) -> str:
        return f"Ticker: {self.ticker}, Shares: {self.__total_shares}, Profit: ${self.__realized_profit:.2f}"
