import funhandler as fh
import time

test_price_data = [
    {
        "type": "price",
        "base": "ETC",
        "trade": "BTC",
        "exchange": "binance",
        "period": "minute",
        "timestamp": time.time(),
    },
    {
        "type": "price",
        "base": "USD",
        "trade": "ETC",
        "exchange": "binance",
        "period": "minute",
        "timestamp": time.time(),
    },
]


def main():
    fh.set_host('localhost')
    fh.set_store_name('test_store_name')
    fh.set_storage_model('local')
    fh.set_local_storage_info(base_path='/tmp', storage_folder='parquet_data')
    fh.initialize_database()
    fh.add_bars(test_price_data)
    fh.load_data(**{
        "type": "price",
        "base": "ETC",
        "trade": "BTC",
        "exchange": "binance",
        "period": "minute"}
    )

    # call funpicker
    # from funpicker import Query, QueryTypes
    # fpq = Query().set_crypto('ETC').set_fiat('BTC').set_exchange('binance').set_period('hour').set_limit(30).get(QueryTypes['price'])

if __name__ == '__main__':
    main()
