"""
Problem: Best Time to Buy and Sell Stock
LeetCode: 121
Pattern: Sliding Window
Time: O(n)
Space: O(1)
Attempts: 1 (solved alone)
Date: 2026-09-22
Notes: Track the lowest price seen and the best profit at each price.
"""

def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0
    
    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
    
    return max_profit
