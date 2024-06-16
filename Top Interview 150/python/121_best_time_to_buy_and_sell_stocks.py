# 169. Majority Element - Easy
"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a 
different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. 
If you cannot achieve any profit, return 0.
"""  # noqa

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, buy_price = 0, prices[0]
        for price in prices[1:]:
            if buy_price > price:
                buy_price = price
            profit = max(profit, price - buy_price)
        return profit


if __name__ == "__main__":
    solution = Solution()
    input_list = [
        [7, 1, 5, 3, 6, 4],
        [7, 6, 4, 3, 1],
        [2, 1, 4],
    ]  # noqa
    expected_output = [5, 0, 3]  # noqa
    actual_output = []
    for input in input_list:
        max_profit = solution.maxProfit(input)
        actual_output.append(max_profit)

    for expected, actual in zip(expected_output, actual_output):
        assert expected == actual
