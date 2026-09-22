"""
Problem: Valid Anagram
LeetCode: 242
Pattern: Frequency Counter
Time: O(n)
Space: O(n)
Attempts: 1 (solved alone)
Date: 2026-09-22
Notes: Compare character frequencies with Counter.
"""

from collections import Counter

def isAnagram(s, t):
    return Counter(s) == Counter(t)
