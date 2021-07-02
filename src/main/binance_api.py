from pprint import pprint

from binance.spot import Spot

client = Spot(base_url='https://testnet.binance.vision',
              key='RCJPWEsM8M3GAf3rS9BxmDel4smYUv2ZwGjEVp4aFLi8kc0lguIRKPqrmoZgB2GD',
              secret='kiqw56MTpd74ARmVl6sX2yYSEZ51PRwx6378RgSRWvWDFMoQumbGohfmq7sEZzsh')


def get_asset_amount(asset):
    b_account = client.account()
    b_balances = b_account['balances']
    return float(next(b_balance['free'] for b_balance in b_balances if b_balance['asset'] == asset))


def get_candles():
    b_klines = client.klines(symbol='BTCUSDT', interval='5m', limit=100)
    klines = []
    for b_kline in b_klines:
        klines.append({
            "open": float(b_kline[1]),
            "high": float(b_kline[2]),
            "low": float(b_kline[3]),
            "close": float(b_kline[4]),
            "asset_volume": float(b_kline[5]),
            "quote_volume": float(b_kline[7])
        })
    return klines


def get_price(asset):
    b_price = client.ticker_price(symbol=asset)
    return float(b_price['price'])


def buy_asset(asset, amount):
    client.new_order(symbol=asset, side='BUY', type='MARKET', quantity=amount)


def sell_asset(asset, amount):
    client.new_order(symbol=asset, side='SELL', type='MARKET', quantity=amount)


if __name__ == '__main__':
    pass
    # print(get_price('BTCUSDT'))
    # buy_asset('BTCUSDT', 1-0.780146)
