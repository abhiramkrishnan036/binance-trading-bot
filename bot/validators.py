import logging

logger = logging.getLogger(__name__)


def validate_symbol(symbol: str) -> str:
    """
    Validate trading symbol format
    Example: BTCUSDT
    """
    if not symbol or len(symbol) < 6:
        raise ValueError("Invalid symbol. Example: BTCUSDT")

    return symbol.upper()


def validate_side(side: str) -> str:
    """
    Validate order side (BUY or SELL)
    """
    side = side.upper()

    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

    return side


def validate_order_type(order_type: str) -> str:
    """
    Validate order type (MARKET or LIMIT)
    """
    order_type = order_type.upper()

    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be MARKET or LIMIT")

    return order_type


def validate_quantity(quantity: float) -> float:
    """
    Validate quantity is positive number
    """
    try:
        quantity = float(quantity)
        if quantity <= 0:
            raise ValueError
    except ValueError:
        raise ValueError("Quantity must be a positive number")

    return quantity


def validate_price(price: float) -> float:
    """
    Validate price is positive number
    """
    try:
        price = float(price)
        if price <= 0:
            raise ValueError
    except ValueError:
        raise ValueError("Price must be a positive number")

    return price