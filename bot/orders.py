from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceOrderException
from bot.logging_config import logger

def place_order(
    client: Client,
    symbol: str,
    side: str,
    order_type: str,
    quantity: float,
    price: float = None,
    stop_price: float = None
) -> dict:
    """
    Places an order on the Binance Futures Testnet.
    Handles MARKET, LIMIT, and STOP_MARKET orders.
    """
    try:
        # Prepare the base order parameters
        params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity
        }

        if order_type == "LIMIT":
            params["timeInForce"] = "GTC"
            params["price"] = price
            logger.info(f"Attempting to place {side} {order_type} order for {quantity} of {symbol}. Params: {params}")
            response = client.futures_create_order(**params)
        elif order_type == "MARKET":
            logger.info(f"Attempting to place {side} {order_type} order for {quantity} of {symbol}. Params: {params}")
            response = client.futures_create_order(**params)
        elif order_type == "STOP_MARKET":
            params["algoType"] = "CONDITIONAL"
            params["triggerPrice"] = stop_price
            logger.info(f"Attempting to place {side} {order_type} ALGO order for {quantity} of {symbol}. Params: {params}")
            response = client.futures_create_algo_order(**params)
        
        logger.info(f"Successfully placed order. Response: {response}")
        return response

    except BinanceAPIException as e:
        logger.error(f"BinanceAPIException: Error placing order. Message: {e.message}, Status Code: {e.status_code}")
        raise
    except BinanceOrderException as e:
        logger.error(f"BinanceOrderException: Error placing order. Message: {e.message}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error placing order: {str(e)}")
        raise
