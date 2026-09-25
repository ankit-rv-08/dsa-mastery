"""
Problem: Top K Frequent Elements
LeetCode: 347
Pattern: Heap / Bucket Sort
Time: O(n) with bucket sort, O(n log k) with heap
Space: O(n)
Attempts: 1 (revision)
Date: 2026-09-24
Notes: Count frequencies with Counter. Either heapq.nlargest or bucket sort
       by frequency. Bucket sort is O(n) — better asymptotically.
"""

from collections import Counter


def topKFrequent(nums, k):
    """Heap approach. O(n log k)."""
    import heapq

    count = Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get)


def topKFrequent_bucket(nums, k):
    """Bucket sort approach. O(n)."""
    count = Counter(nums)
    buckets = [[] for _ in range(len(nums) + 1)]
    for num, freq in count.items():
        buckets[freq].append(num)
    result = []
    for i in range(len(buckets) - 1, 0, -1):
        for num in buckets[i]:
            result.append(num)
            if len(result) == k:
                return result
    return result


if __name__ == "__main__":
    print(topKFrequent([1, 1, 1, 2, 2, 3], 2))          # [1, 2]
    print(topKFrequent_bucket([1, 1, 1, 2, 2, 3], 2))   # [1, 2]
    print(topKFrequent([1], 1))                          # [1]
