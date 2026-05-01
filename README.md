# Binance Futures Testnet Trading Bot

A Python-based CLI trading bot that interacts with the Binance Futures Testnet (USDT-M) to place Market, Limit, and Stop-Market orders.

## Features
- **Orders**: Place `MARKET`, `LIMIT`, and `STOP_MARKET` orders.
- **Strict Validation**: Input validation to ensure safe execution.
- **Granular Error Handling**: Specific handling for Binance API errors, network issues, and input validation.
- **Robust Logging**: Structured logging separation between file and console.

## Setup Instructions

1. **Clone the repository / Extract the folder**

2. **Create a virtual environment (Recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables**
   Create a `.env` file in the root directory:
   ```env
   BINANCE_API_KEY=your_api_key
   BINANCE_API_SECRET=your_secret_key
   # The bot is configured to automatically route to the testnet via the python-binance library
   ```

## How to Run Examples

Use the Typer-based CLI to place orders. You can use `--help` to see all options:
```bash
python cli.py place-order --help
```

### 1. Market Order
```bash
python cli.py place-order --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### 2. Limit Order
Requires `--price`.
```bash
python cli.py place-order --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 90000
```

### 3. Stop-Market Order (Bonus)
Requires `--stop-price`.
*Note: Binance Futures requires a minimum notional value (Price × Quantity), typically ≥ 100 USDT. We use `0.003` here because `50,000 * 0.003 = 150`.*
```bash
python cli.py place-order --symbol BTCUSDT --side SELL --type STOP_MARKET --quantity 0.003 --stop-price 50000
```

## Sample Output

```text
Success! Order placed successfully on Binance Futures Testnet.

        Order Summary         
+----------------------------+
| Property     | Value       |
|--------------+-------------|
| Symbol       | BTCUSDT     |
| Side         | BUY         |
| Type         | MARKET      |
| Order ID     | 13095872880 |
| Status       | FILLED      |
| Executed Qty | 0.001       |
| Avg Price    | 77150.25    |
+----------------------------+
```

## Logs
Logs are saved in `trading_bot.log`. 
- **Console Output**: Provides clean, colored summaries of your actions without noisy raw JSON.
- **File Output**: Contains structured, detailed logs of API request attempts, responses, and errors with full context for debugging.

## Assumptions
When developing and testing this bot, the following assumptions were made:
1. **Account Balance**: It is assumed the user has successfully generated testnet API keys and has sufficient testnet USDT balance to place orders.
2. **Notional Value Limits**: It is assumed the user will input quantities large enough to satisfy Binance's minimum notional value requirements (Price × Quantity ≥ 100 USDT) when testing.
