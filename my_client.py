from binance.client import Client
import config

class BinanceClient:
    def __init__(self, api_key, api_secret):
        if not api_key or not api_secret:
            raise ValueError("API key and secret must be provided. Set BINANCE_API_KEY and BINANCE_API_SECRET.")

        self.client = Client(
            api_key,
            api_secret,
            testnet=config.TESTNET,
            base_endpoint=config.BASE_URL if config.TESTNET else ""
        )

    # ✅ Get current price
    def get_price(self, symbol):
        try:
            ticker = self.client.get_symbol_ticker(symbol=symbol)
            return float(ticker["price"])
        except Exception as e:
            print(f"Error fetching price: {e}")
            return None

    # ✅ Place market order
    def place_order(self, symbol, side, quantity):
        try:
            if side.upper() == "BUY":
                order = self.client.order_market_buy(
                    symbol=symbol,
                    quantity=quantity
                )
            elif side.upper() == "SELL":
                order = self.client.order_market_sell(
                    symbol=symbol,
                    quantity=quantity
                )
            else:
                print("Invalid side (must be BUY or SELL)")
                return

            print("✅ Order placed successfully!")
            print(order)

        except Exception as e:
            print(f"Error placing order: {e}")