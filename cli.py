import typer
from rich.console import Console
from rich.table import Table

from bot.client import get_binance_client
from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
    validate_stop_price
)
from bot.orders import place_order
from bot.logging_config import logger
from binance.exceptions import BinanceAPIException, BinanceOrderException

app = typer.Typer(help="Binance Futures Testnet Trading Bot CLI")
console = Console()

@app.callback()
def callback():
    pass

@app.command(name="place-order")
def place_order_cmd(
    symbol: str = typer.Option(..., "--symbol", help="Trading pair symbol, e.g., BTCUSDT"),
    side: str = typer.Option(..., "--side", help="Order side: BUY or SELL"),
    order_type: str = typer.Option(..., "--type", help="Order type: MARKET, LIMIT, STOP_MARKET"),
    quantity: float = typer.Option(..., "--quantity", help="Amount to trade"),
    price: float = typer.Option(None, "--price", help="Required for LIMIT orders"),
    stop_price: float = typer.Option(None, "--stop-price", help="Required for STOP_MARKET orders"),
):
    try:
        val_symbol = validate_symbol(symbol)
        val_side = validate_side(side)
        val_type = validate_order_type(order_type)
        val_quantity = validate_quantity(quantity)
        val_price = validate_price(price, val_type)
        val_stop_price = validate_stop_price(stop_price, val_type)

        client = get_binance_client()

        response = place_order(
            client=client,
            symbol=val_symbol,
            side=val_side,
            order_type=val_type,
            quantity=val_quantity,
            price=val_price,
            stop_price=val_stop_price
        )

        console.print(f"\n[bold green]Success![/bold green] Order placed successfully on Binance Futures Testnet.")
        
        table = Table(title="Order Summary", show_header=True, header_style="bold magenta")
        table.add_column("Property", style="cyan")
        table.add_column("Value", style="white")

        order_id = str(response.get("orderId", response.get("algoId", "N/A")))
        status = response.get("status", response.get("algoStatus", "N/A"))
        executed_qty = str(response.get("executedQty", "0"))
        avg_price = str(response.get("avgPrice", "0"))

        table.add_row("Symbol", val_symbol)
        table.add_row("Side", val_side)
        table.add_row("Type", val_type)
        table.add_row("Order ID", order_id)
        table.add_row("Status", status)
        table.add_row("Executed Qty", executed_qty)
        table.add_row("Avg Price", avg_price)

        console.print(table)

    except ValueError as ve:
        console.print(f"[bold red]Validation Error:[/bold red] {str(ve)}")
        logger.warning(f"Validation failed: {str(ve)}")
    except BinanceAPIException as bae:
        console.print(f"[bold red]Binance API Error:[/bold red] {bae.message} (Status: {bae.status_code})")
    except BinanceOrderException as boe:
        console.print(f"[bold red]Binance Order Error:[/bold red] {boe.message}")
    except Exception as e:
        console.print(f"[bold red]An unexpected error occurred:[/bold red] {str(e)}")

if __name__ == "__main__":
    app()
