# TradeAttributes
Application that processes a stream of trades and generates a summary

#### Input Format:
- TimeStamp,Symbol,Quantity,Price

#### Input Format Definitions
- TimeStamp is value indicating the microseconds since midnight.
- Symbol is the 3 character unique identifier for a financial 
  instrument (Stock, future etc.)
- Quantity is the amount traded
- Price is the price of the trade for that financial instrument.

#### Output Format:
- symbol,MaxTimeGap,Volume,WeightedAveragePrice,MaxPrice

#### Output Format Definitions
- MaxTimeGap is the amount of time that passes between trades of a symbol
  If only 1 trade then the gap is 0
- Volume is total volume traded (sum of the quantity for all trades
  in a symbol)
- WeightedAveragePrice is the average price per unit traded overall,
  with result truncated to a whole number.
- MaxPrice is the highest single trade price


#### Application Assumptions:
- TimeStamp is always for the same day and won't roll over midnight.
- TimeStamp is increasing or same as previous tick (time gap will never be < 0).
- Price - our currency is an integer based currency.  No decimal points.
- Price - Price is always > 0.

