import keys.keys as keys
from time_operators.time_operator import TimeOperator
from bots.spot_grid import StaticGridBot
from config.intervals import INTERVALS
import os

units = 0.001
position = 0
tc = -0.00085

time = TimeOperator()

available_strategies = ["triple_sma", "triple_ema", "macd", "rsi", "ichimoku_cloud"]
symbols = ["BTCUSDT", "ADAUSDT", "SANDUSDT", "MBOXUSDT", "ETHUSDT", "DOTUSDT", "SOLUSDT"]

strategy = "triple_sma"
period_cagr = "month"
fee = 0.1

bot = StaticGridBot(key=keys.testnet_api_key,
                    secret=keys.testnet_secret_key,
                    use_testnet=True,
                    base_symbol="eth",
                    quote_symbol="usdt",
                    units=0.01,
                    fee=fee,
                    upper_price=1380.00,
                    lower_price=1280.00,
                    num_grids=8,
                    stop_loss_active=True,
                    stop_loss=1250.00,
                    take_profit_active=True,
                    take_profit=1450.0,
                    sale_base_asset=False,
                    )

bot.start_grid_bot_trading()