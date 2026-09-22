"""
Problem: Group Anagrams
LeetCode: 49
Pattern: Hash Map + Sorted Key
Time: O(n * k log k) where n = number of strings, k = max string length
Space: O(n * k)
Attempts: 1 (revision)
Date: 2026-09-23
Notes: Sort each string to get a canonical key. Group by key.
    Alternative: use a 26-length character count tuple as the key (O(n*k)).
"""

from collections import defaultdict

def groupAnagrams(strs):
    groups = defaultdict(list)

    for s in strs:
        key = "".join(sorted(s))
        groups[key].append(s)
    return list(groups.values())

def groupAnagrams_count(strs):
    groups = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for char in s:
            count[ord(char) - ord("a")] += 1
        groups[tuple(count)].append(s)
    return list(groups.values())

if __name__ == "__main__":
    print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    # [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
