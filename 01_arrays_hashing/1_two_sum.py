"""
Problem: Two Sum
LeetCode: 1
Pattern: Hash Map (complement lookup)
Time: O(n)
Space: O(n)
Attempts: 1 (revision)
Date: 2026-09-23
Notes: Store value -> index. For each num, check if target - num is already seen.
"""

def twoSum(nums, target):
    seen = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in seen:
            return [seen[complement], i]
        
        seen[num] = i
    
    return []

if __name__ == "__main__":
    print(twoSum([3, 4, 5, 6], 7))   # [0, 1]
    print(twoSum([4, 5, 6], 10))     # [0, 2]
    print(twoSum([5, 5], 10))        # [0, 1]
