import keys.keys as keys
from time_operators.time_operator import TimeOperator
from bots.ta_bots.ema_crossover import EMACrossoverBOT
# from bots.bot import Bot
from bots.grid.spot_grid import StaticGridBot
from config.title import TITLE
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
                    base_symbol="btc",
                    quote_symbol="usdt",
                    units=0.001,
                    fee=fee,
                    upper_price=30000.00,
                    lower_price=24000.00,
                    num_grids=8,
                    stop_loss_active=True,
                    stop_loss=25000.00,
                    take_profit_active=True,
                    take_profit=30000.0,
                    sale_base_asset=False,
                    )

bot.start_grid_bot_trading()