import argparse
from bot.logging_config import setup_logging
from bot.orders import OrderManager

# Initialize logging
logger = setup_logging()


def main():
    parser = argparse.ArgumentParser(description="Binance Futures Demo Trading Bot")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", required=True, type=float)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        order_manager = OrderManager()

        response = order_manager.place_order(
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price
        )

        print("\nOrder placed successfully!")
        print("Order ID:", response.get("orderId"))
        print("Status:", response.get("status"))
        print("Executed Quantity:", response.get("executedQty"))
        print("Average Price:", response.get("avgPrice", "N/A"))

    except Exception as e:
        print("\nOrder failed:", str(e))


if __name__ == "__main__":
    main()