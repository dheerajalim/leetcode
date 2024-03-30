def max_profit(prices):
    # sell should always be future index
    n = len(prices)

    # if there is only one price, then we cannot sell it int the future days
    if n == 1:
        return 0

    # keep the buy and sell prices on day 0 and day 1
    buy, sell = 0, 1
    # to store the max profit
    max_profit = 0

    # we iterate until we reach the last  day of the prices
    while sell < n:
        # if the buying prices is less than the selling price
        # this means its profit, se we update  the max profit
        if prices[buy] < prices[sell]:
            max_profit = max(max_profit, prices[sell] - prices[buy])
            # and since our buying price is already less, we move our selling price
            sell += 1

        # else if the buying price is greater than selling price, then this is a loss
        # ,so we move our buy pointer to sell pointer and sell pointer to next day
        # this way we now point to the lower buying price then previous amount
        else:
            buy = sell
            sell += 1

    return max_profit


prices = [7, 1, 5, 3, 6, 4]
prices = [10, 2, 3, 4, 5, 6, 1]

print(max_profit(prices))
