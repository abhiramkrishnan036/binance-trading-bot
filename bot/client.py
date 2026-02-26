import os
import logging
from binance.client import Client
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

logger = logging.getLogger(__name__)


class BinanceClient:
    """
    Binance Futures Demo Client Wrapper
    """

    def __init__(self):
        try:
            self.api_key = os.getenv("API_KEY")
            self.api_secret = os.getenv("API_SECRET")
            self.base_url = os.getenv("BASE_URL")

            if not self.api_key or not self.api_secret:
                raise ValueError("API credentials not found in .env file")

            # Initialize Binance client
            self.client = Client(
                api_key=self.api_key,
                api_secret=self.api_secret
            )

            # IMPORTANT: Set Demo Futures API endpoint
            self.client.FUTURES_URL = self.base_url + "/fapi"

            logger.info("Binance Demo Futures client initialized successfully")

        except Exception as e:
            logger.error(f"Client initialization failed: {e}")
            raise

    def place_market_order(self, symbol, side, quantity):
        try:
            logger.info(f"Placing MARKET order: {side} {quantity} {symbol}")

            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

            return order

        except Exception as e:
            logger.error(f"Market order failed: {e}")
            raise

    def place_limit_order(self, symbol, side, quantity, price):
        try:
            logger.info(f"Placing LIMIT order: {side} {quantity} {symbol} at {price}")

            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

            return order

        except Exception as e:
            logger.error(f"Limit order failed: {e}")
            raise