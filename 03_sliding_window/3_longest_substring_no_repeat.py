"""
Problem: Longest Substring Without Repeating Characters
LeetCode: 3
Pattern: Sliding Window
Time: O(n)
Space: O(n)
Attempts: 1 (solved alone)
Date: 2026-09-22
Notes: Shrink the window until its set contains no duplicate character.
"""

def lengthOfLongestSubstring(s):
    char_set = set()
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    
    return max_length
