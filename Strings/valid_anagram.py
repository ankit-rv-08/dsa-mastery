"""
LeetCode #242: Valid Anagram
Pattern: HashMap Frequency
Date: Oct 26, 2025
"""

from collections import Counter

def isAnagram(s, t):
    return Counter(s) == Counter(t)
