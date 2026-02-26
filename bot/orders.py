import logging
from bot.client import BinanceClient
from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)

logger = logging.getLogger(__name__)


class OrderManager:
    """
    Handles order placement logic
    """

    def __init__(self):
        self.client = BinanceClient()

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            # Validate inputs
            symbol = validate_symbol(symbol)
            side = validate_side(side)
            order_type = validate_order_type(order_type)
            quantity = validate_quantity(quantity)

            if order_type == "LIMIT":
                if price is None:
                    raise ValueError("Price required for LIMIT order")
                price = validate_price(price)

            logger.info(f"Order Request: {symbol} {side} {order_type} Qty={quantity} Price={price}")

            # Place order
            if order_type == "MARKET":
                response = self.client.place_market_order(
                    symbol=symbol,
                    side=side,
                    quantity=quantity
                )
            else:
                response = self.client.place_limit_order(
                    symbol=symbol,
                    side=side,
                    quantity=quantity,
                    price=price
                )

            logger.info(f"Order Response: {response}")

            return response

        except Exception as e:
            logger.error(f"Order failed: {e}")
            raise