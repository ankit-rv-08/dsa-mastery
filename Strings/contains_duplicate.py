"""
LeetCode #217: Contains Duplicate
Pattern: Set
Date: Oct 26, 2025
"""

def containsDuplicate(nums):
    return len(set(nums)) != len(nums)
