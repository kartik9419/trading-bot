from my_client import BinanceClient
from strategy import simple_strategy
from logger import setup_logger
import config


def main():
    logger = setup_logger()

    client = BinanceClient(config.API_KEY, config.API_SECRET)

    print("=== Binance Testnet Trading Bot ===")

    symbol = input("Enter symbol (e.g. BTCUSDT): ").upper()
    quantity = float(input("Enter quantity: "))

    try:
        price = client.get_price(symbol)

        signal = simple_strategy(price)
        print(f"Generated Signal: {signal}")

        confirm = input("Do you want to place order? (yes/no): ").lower()

        if confirm == "yes":
            client.place_order(symbol, signal, quantity)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()