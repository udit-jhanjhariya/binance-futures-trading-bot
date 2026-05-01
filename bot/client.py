import os
from binance.client import Client
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_binance_client() -> Client:
    """
    Initializes and returns a python-binance Client configured
    for the Binance Futures Testnet.
    """
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")

    if not api_key or not api_secret:
        raise ValueError(
            "Missing Binance API Credentials. "
            "Please ensure BINANCE_API_KEY and BINANCE_API_SECRET are set in the .env file."
        )

    # Initialize client
    client = Client(api_key, api_secret, testnet=True)
    return client
