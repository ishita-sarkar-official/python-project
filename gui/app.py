import tkinter as tk
from tkinter import ttk, messagebox
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dotenv import load_dotenv
from bot.bot import BasicBot
from bot.utils import setup_logger

load_dotenv(dotenv_path='config/.env')
setup_logger()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
BASE_URL = os.getenv("TESTNET_URL")

bot = BasicBot(API_KEY, API_SECRET, BASE_URL)

# GUI Application
class TradingApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Binance Futures Trading Bot")
        self.geometry("400x420")
        self.resizable(False, False)
        self.create_widgets()

    def create_widgets(self):
        # Symbol
        tk.Label(self, text="Symbol (e.g., BTCUSDT):").pack(pady=(10, 0))
        self.symbol_entry = tk.Entry(self)
        self.symbol_entry.pack()

        # Side
        tk.Label(self, text="Side (buy/sell):").pack(pady=(10, 0))
        self.side_entry = tk.Entry(self)
        self.side_entry.pack()

        # Order Type
        tk.Label(self, text="Order Type:").pack(pady=(10, 0))
        self.order_type = ttk.Combobox(
            self,
            values=["MARKET", "LIMIT", "STOP", "STOP_MARKET"],
            state="readonly"
        )
        self.order_type.current(0)
        self.order_type.pack()

        # Quantity
        tk.Label(self, text="Quantity:").pack(pady=(10, 0))
        self.quantity_entry = tk.Entry(self)
        self.quantity_entry.pack()

        # Price (for LIMIT or STOP)
        tk.Label(self, text="Price (Limit/Stop only):").pack(pady=(10, 0))
        self.price_entry = tk.Entry(self)
        self.price_entry.pack()

        # Stop Price (for STOP or STOP_MARKET)
        tk.Label(self, text="Stop Price (Stop/Stop-Market only):").pack(pady=(10, 0))
        self.stop_price_entry = tk.Entry(self)
        self.stop_price_entry.pack()

        # Submit Button
        tk.Button(self, text="Place Order", command=self.place_order).pack(pady=20)

    def place_order(self):
        try:
            symbol = self.symbol_entry.get().strip().upper()
            side = self.side_entry.get().strip().lower()
            order_type = self.order_type.get().strip().upper()
            quantity = float(self.quantity_entry.get().strip())
            price = self.price_entry.get().strip()
            stop_price = self.stop_price_entry.get().strip()

            price = float(price) if price else None
            stop_price = float(stop_price) if stop_price else None

            order = bot.place_order(symbol, side, order_type, quantity, price, stop_price)

            if order:
                messagebox.showinfo("Success", f"Order placed:\nOrder ID: {order['orderId']}")
            else:
                messagebox.showerror("Failed", "Order could not be placed. See logs.")

        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numeric values.")
        except Exception as e:
            messagebox.showerror("Error", f"Unexpected error:\n{str(e)}")

if __name__ == "__main__":
    app = TradingApp()
    app.mainloop()
