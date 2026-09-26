"""
Problem: Longest Consecutive Sequence
LeetCode: 128
Pattern: Hash Set + smart iteration
Time: O(n)
Space: O(n)
Attempts: 1
Date: 2026-09-25
Notes: Set lookup. Only start counting from sequence beginnings (num - 1 not in set).
"""


def longestConsecutive(nums):
    if not nums:
        return 0
    num_set = set(nums)
    longest = 0
    for num in num_set:
        if num - 1 not in num_set:
            current = num
            length = 1
            while current + 1 in num_set:
                current += 1
                length += 1
            longest = max(longest, length)
    return longest


if __name__ == "__main__":
    print(longestConsecutive([100, 4, 200, 1, 3, 2]))  # 4
    print(longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # 9
    print(longestConsecutive([1, 0, 1, 2]))  # 3
    print(longestConsecutive([]))  # 0
