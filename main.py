import os
from dotenv import load_dotenv
from bot.bot import BasicBot
from bot.utils import setup_logger

def get_user_input():
    print("\n=== Binance Futures Trading Bot ===")
    symbol = input("Enter trading pair (e.g., BTCUSDT): ").upper()
    side = input("Enter side (buy/sell): ").lower()
    order_type = input("Enter order type (MARKET/LIMIT): ").upper()
    quantity = float(input("Enter quantity: "))
    price = None
    if order_type == "LIMIT":
        price = float(input("Enter price: "))
    return symbol, side, order_type, quantity, price

def main():
    setup_logger()
    load_dotenv(dotenv_path='config/.env')
    api_key = os.getenv("API_KEY")
    api_secret = os.getenv("API_SECRET")
    base_url = os.getenv("TESTNET_URL")

    bot = BasicBot(api_key, api_secret, base_url)

    while True:
        symbol, side, order_type, quantity, price = get_user_input()
        order = bot.place_order(symbol, side, order_type, quantity, price)
        if order:
            print("Order placed successfully!")
        else:
            print("Failed to place order.")
        cont = input("Place another order? (y/n): ").lower()
        if cont != 'y':
            break

if __name__ == "__main__":
    main()
