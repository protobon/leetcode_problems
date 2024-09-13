from typing import List


def max_profit(prices: List[int]) -> int:
    min_price = prices[0]
    profit = 0
    for price in prices:
        if price - min_price > profit:
            profit = price - min_price
        if price < min_price:
            min_price = price

    return profit


prices = [7,1,5,3,6,4]
print(max_profit(prices))
prices = [7,6,4,3,1]
print(max_profit(prices))
