"""
Hour 4 – Two Sum Problem (Brute Force & Hash Map)
"""

def two_sum_brute(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

def two_sum_map(nums, target):
    lookup = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in lookup:
            return [lookup[complement], i]
        lookup[num] = i
    return []

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(two_sum_brute(nums, target))  # [0, 1]
    print(two_sum_map(nums, target))    # [0, 1]
