"""
Problem: Two Sum
LeetCode: 1
Pattern: Hash Map
Time: O(n)
Space: O(n)
Attempts: 1 (solved alone)
Date: 2026-09-22
Notes: Store each number's index and check for its complement.
"""

def twoSum(nums, target):
    seen = {}  # {value: index}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in seen:
            return [seen[complement], i]
        
        seen[num] = i
    
    return []

if __name__ == "__main__":
    print(twoSum([2,7,11,15], 9))  # [0, 1]
    print(twoSum([3,2,4], 6))      # [1, 2]
    print(twoSum([3,3], 6))        # [0, 1]
