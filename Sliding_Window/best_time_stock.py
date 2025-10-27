"""
LeetCode #121: Best Time to Buy and Sell Stock
Pattern: Sliding Window (Track Min)
Date: Oct 27, 2025
"""

def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0
    
    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
    
    return max_profit
