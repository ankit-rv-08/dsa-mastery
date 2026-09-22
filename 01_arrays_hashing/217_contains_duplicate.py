"""
Problem: Contains Duplicate
LeetCode: 217
Pattern: Hash Set
Time: O(n)
Space: O(n)
Attempts: 1 (solved alone)
Date: 2026-09-22
Notes: Used a set. Check if num in seen before adding.
"""

def containsDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

if __name__ == "__main__":
    print(containsDuplicate([1, 2, 3, 1]))  # True
    print(containsDuplicate([1, 2, 3, 4]))  # False
    print(containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  # True
