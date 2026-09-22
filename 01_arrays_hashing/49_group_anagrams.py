"""
Problem: Group Anagrams
LeetCode: 49
Pattern: Sorted Key
Time: O(n * k log k)
Space: O(n * k)
Attempts: 1 (solved alone)
Date: 2026-09-22
Notes: Use each word's sorted characters as the dictionary key.
"""

from collections import defaultdict

def groupAnagrams(strs):
    groups = defaultdict(list)
    
    for word in strs:
        sorted_word = ''.join(sorted(word))
        groups[sorted_word].append(word)
    
    return list(groups.values())
