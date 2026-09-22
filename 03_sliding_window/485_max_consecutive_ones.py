"""
Problem: Max Consecutive Ones
LeetCode: 485
Pattern: Sliding Window
Time: O(n)
Space: O(1)
Attempts: 1 (solved alone)
Date: 2026-09-22
Notes: Count the current run of ones and retain the longest run.
"""

def findMaxConsecutiveOnes(nums):
    max_count = 0
    current = 0
    
    for num in nums:
        if num == 1:
            current += 1
            max_count = max(max_count, current)
        else:
            current = 0
    
    return max_count
