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
   - Copy the example environment file:
     ```bash
     cp .env.example .env
     ```
   - Edit `.env` and insert your Binance Futures Testnet API Key and Secret.

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
*Note: Binance Futures Testnet requires orders to have a notional value (Price × Quantity) of at least 100 USDT. We use `0.003` here because `50,000 * 0.003 = 150`.*
```bash
python cli.py place-order --symbol BTCUSDT --side SELL --type STOP_MARKET --quantity 0.003 --stop-price 50000
```

## Logs
Logs are saved in `trading_bot.log`. 
- **Console Output**: Provides clean, colored summaries of your actions without noisy raw JSON.
- **File Output**: Contains structured, detailed logs of API request attempts, responses, and errors with full context for debugging.
