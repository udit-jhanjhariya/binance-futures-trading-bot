import os
from binance.client import Client
from dotenv import load_dotenv

load_dotenv()

def get_binance_client() -> Client:
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")
    if not api_key or not api_secret:
        raise ValueError(
            "Missing Binance API Credentials. "
            "Please ensure BINANCE_API_KEY and BINANCE_API_SECRET are set in the .env file."
        )
    client = Client(api_key, api_secret, testnet=True)
    return client
