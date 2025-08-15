"""
Hour 4 – Sliding Window: Maximum Sum Subarray (Fixed Size)
"""

def max_sum_subarray(nums, k):
    max_sum = curr_sum = sum(nums[:k])
    for i in range(k, len(nums)):
        curr_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, curr_sum)
    return max_sum

if __name__ == "__main__":
    nums = [1, 4, 2, 10, 2, 3, 1, 0, 20]
    k = 4
    print(max_sum_subarray(nums, k))  # Output: 24
