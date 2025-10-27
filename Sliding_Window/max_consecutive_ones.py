"""
LeetCode #485: Max Consecutive Ones
Pattern: Sliding Window
Date: Oct 27, 2025
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
