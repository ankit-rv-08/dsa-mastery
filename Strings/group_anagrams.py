"""
LeetCode #49: Group Anagrams
Pattern: Sorted Key + defaultdict
Date: Oct 26, 2025
"""

from collections import defaultdict

def groupAnagrams(strs):
    groups = defaultdict(list)
    
    for word in strs:
        sorted_word = ''.join(sorted(word))
        groups[sorted_word].append(word)
    
    return list(groups.values())
