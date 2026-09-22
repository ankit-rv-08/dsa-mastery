"""
Problem: Valid Anagram
LeetCode: 242
Pattern: Frequency Count
Time: O(n)
Space: O(n)
Attempts: 1 (solved alone)
Date: 2026-09-22
Notes: Counter(s) == Counter(t) is O(n). sorted comparison is O(n log n).
    Counter is faster; sorted is simpler.
"""

from collections import Counter

def isAnagram(s, t):
    return Counter(s) == Counter(t)

def isAnagram_sorted(s, t):
    return sorted(s) == sorted(t)

if __name__ == "__main__":
    print(isAnagram("anagram", "nagaram"))  # True
    print(isAnagram("rat", "car"))          # False
