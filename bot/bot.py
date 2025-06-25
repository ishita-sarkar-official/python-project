from binance.client import Client
from binance.enums import *
import logging

class BasicBot:
    def __init__(self, api_key, api_secret, base_url):
        self.client = Client(api_key, api_secret)
        self.client.FUTURES_URL = base_url
        self.client.API_URL = base_url
        logging.info("Bot initialized with testnet URL.")

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            params = {
                'symbol': symbol,
                'side': SIDE_BUY if side.lower() == 'buy' else SIDE_SELL,
                'type': order_type,
                'quantity': quantity
            }
            if order_type == ORDER_TYPE_LIMIT:
                params['timeInForce'] = TIME_IN_FORCE_GTC
                params['price'] = price

            order = self.client.futures_create_order(**params)
            logging.info(f"Order placed: {order}")
            return order
        except Exception as e:
            logging.error(f"Order error: {e}")
            return None
