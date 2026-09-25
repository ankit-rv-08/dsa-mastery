"""
Problem: Product of Array Except Self
LeetCode: 238
Pattern: Prefix / Suffix Products
Time: O(n)
Space: O(1) extra (output array doesn't count)
Attempts: 1 (revision)
Date: 2026-09-24
Notes: Two passes. First fills output[i] with left product. Second
       multiplies by right product. No division — handles zeros safely.
"""


def productExceptSelf(nums):
    n = len(nums)
    output = [1] * n

    prefix = 1
    for i in range(n):
        output[i] = prefix
        prefix *= nums[i]

    suffix = 1
    for i in range(n - 1, -1, -1):
        output[i] *= suffix
        suffix *= nums[i]

    return output


if __name__ == "__main__":
    print(productExceptSelf([1, 2, 3, 4]))     # [24, 12, 8, 6]
    print(productExceptSelf([-1, 1, 0, -3, 3]))  # [0, 0, 9, 0, 0]
    print(productExceptSelf([2, 3]))            # [3, 2]
