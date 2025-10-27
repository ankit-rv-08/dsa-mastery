"""
LeetCode #1: Two Sum
Difficulty: Easy
Pattern: HashMap
Date Solved: October 26, 2025
Time Complexity: O(n)
Space Complexity: O(n)

Problem:
Given an array of integers nums and an integer target, return indices of 
the two numbers such that they add up to target.

Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: nums[0] + nums[1] = 2 + 7 = 9
"""

def twoSum(nums, target):
    """
    HashMap approach: Store what we've seen, check for complement
    """
    seen = {}  # {value: index}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in seen:
            return [seen[complement], i]
        
        seen[num] = i
    
    return []

# Test cases
if __name__ == "__main__":
    print(twoSum([2,7,11,15], 9))  # [0, 1]
    print(twoSum([3,2,4], 6))      # [1, 2]
    print(twoSum([3,3], 6))        # [0, 1]
