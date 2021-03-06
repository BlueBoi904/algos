"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that
stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

"""


def maxProfit(prices):
    # Buy low, sell high
    maxSeenProfit = 0
    for i in range(len(prices)):
        buy = prices[i]
        for j in range(i + 1, len(prices)):

            sell = prices[j]
            print(buy, sell)
            profit = sell - buy
            if profit > maxSeenProfit:
                maxSeenProfit = profit
    print('end')
    return maxSeenProfit


def maxProfit2(prices):
    min_price = float('inf')
    max_profit = 0
    for i in range(len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        elif prices[i] - min_price > max_profit:
            max_profit = prices[i] - min_price

    return max_profit


maxProfit([7, 1, 5, 3, 6, 4])
maxProfit2([7, 1, 5, 3, 6, 4])
