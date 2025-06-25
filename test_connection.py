from binance.client import Client
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path='config/.env')

api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")
base_url = os.getenv("TESTNET_URL")

client = Client(api_key, api_secret)
client.FUTURES_URL = base_url
client.API_URL = base_url

try:
    account = client.futures_account()
    print("Connected successfully!")
    print(f"Wallet balance: {account['totalWalletBalance']} USDT")
except Exception as e:
    print("Connection failed:")
    print(e)
