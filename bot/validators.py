def validate_symbol(symbol: str) -> str:
    if not isinstance(symbol, str) or not symbol.strip():
        raise ValueError(f"Invalid symbol: '{symbol}'. Must be a valid string like 'BTCUSDT'.")
    return symbol.upper().strip()

def validate_side(side: str) -> str:
    side_upper = side.upper().strip()
    if side_upper not in ["BUY", "SELL"]:
        raise ValueError(f"Invalid side: '{side}'. Must be exactly 'BUY' or 'SELL'.")
    return side_upper

def validate_order_type(order_type: str) -> str:
    type_upper = order_type.upper().strip()
    valid_types = ["MARKET", "LIMIT", "STOP_MARKET"]
    if type_upper not in valid_types:
        raise ValueError(f"Invalid order type: '{order_type}'. Must be one of {valid_types}.")
    return type_upper

def validate_quantity(quantity: float) -> float:
    try:
        q = float(quantity)
        if q <= 0:
            raise ValueError()
        return q
    except ValueError:
        raise ValueError(f"Invalid quantity: '{quantity}'. Must be a float greater than 0.")

def validate_price(price: float, order_type: str) -> float:
    if order_type == "LIMIT":
        if price is None:
            raise ValueError("Price is required for LIMIT orders.")
        try:
            p = float(price)
            if p <= 0:
                raise ValueError()
            return p
        except ValueError:
            raise ValueError(f"Invalid price: '{price}'. Must be a float greater than 0.")
    return None

def validate_stop_price(stop_price: float, order_type: str) -> float:
    if order_type == "STOP_MARKET":
        if stop_price is None:
            raise ValueError("Stop Price is required for STOP_MARKET orders.")
        try:
            p = float(stop_price)
            if p <= 0:
                raise ValueError()
            return p
        except ValueError:
            raise ValueError(f"Invalid stop price: '{stop_price}'. Must be a float greater than 0.")
    return None
