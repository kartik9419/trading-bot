import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")
TESTNET = os.getenv("BINANCE_TESTNET", "True").strip().lower() in ("true", "1", "yes")
BASE_URL = "https://testnet.binance.vision" if TESTNET else ""