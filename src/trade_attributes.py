
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)-8s %(message)s')
logger = logging.getLogger()


def process_file():
    """
    Main processing - grabs local file 'input.csv', outputs locally 'output.csv'

    Major assumption of this process is that 'TimeStamp is increasing or same as previous tick'
    """

    logger.info("process_file initiated, starting file read")

    # Totals tracking, key for each is symbol
    last_trade_time = {}  # tracking for max_time_between_trades
    max_time_between_trades = {}
    total_volume_traded = {}
    max_trade_price = {}
    weighted_avg_top = {}

    with open("input.csv", "r") as read_file:

        for line in read_file:

            payload = line.strip()
            payload_items = payload.split(",")

            # If we have too many items, we can continue ignoring extra fields, but not enough needs to be bypassed
            if len(payload_items) < 4:
                logger.error("Too few fields to process line: '" + payload + "'")
                continue

            # Name and parse the fields
            microseconds_since_midnight = int(payload_items[0])
            symbol = payload_items[1].strip()
            quantity_traded = int(payload_items[2])
            price_of_trade = int(payload_items[3])

            # Check for time since last trade for this symbol
            if symbol not in max_time_between_trades:
                max_time_between_trades[symbol] = 0
            else:
                time_since_last_trade = microseconds_since_midnight - last_trade_time[symbol]
                if time_since_last_trade > max_time_between_trades[symbol]:
                    max_time_between_trades[symbol] = time_since_last_trade
            last_trade_time[symbol] = microseconds_since_midnight

            # Add to the totals for volume
            total_volume_traded[symbol] = total_volume_traded.get(symbol, 0) + quantity_traded

            # Check for max trade price
            if price_of_trade > max_trade_price.get(symbol, 0):
                max_trade_price[symbol] = price_of_trade

            # Add to the weighted average tracking
            weighted_avg_top[symbol] = weighted_avg_top.get(symbol, 0) + (quantity_traded * price_of_trade)

    logger.info("File read complete, writing output")

    with open("output.csv", "w") as write_file:
        for symbol in sorted(max_time_between_trades.keys()):
            write_file.write(",".join([symbol,
                                       str(max_time_between_trades[symbol]),
                                       str(total_volume_traded[symbol]),
                                       str(round(weighted_avg_top[symbol] / total_volume_traded[symbol])),
                                       str(max_trade_price[symbol])
                                       ])
                             + "\n")

    logger.info("process_file completed")


if __name__ == '__main__':

    logger.info("Application logging is configured")
    process_file()
