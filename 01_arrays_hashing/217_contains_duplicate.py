"""
Problem: Contains Duplicate
LeetCode: 217
Pattern: Hash Set
Time: O(n)
Space: O(n)
Attempts: 1 (solved alone)
Date: 2026-09-22
Notes: Compare the input length with the length of its set of values.
"""

def containsDuplicate(nums):
    return len(set(nums)) != len(nums)
