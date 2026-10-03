"""
Problem: Container With Most Water
LeetCode: 11
Pattern: Two Pointers (converging)
Time: O(n)
Space: O(1)
Attempts: 1
Date: 2026-10-03
Notes: Start with widest container. Move the pointer at the shorter line
       inward — moving the taller line can't increase area.
"""

def maxArea(height):
    left = 0
    right = len(height) - 1
    max_water = 0

    while left < right:
        width = right - left
        h = min(height[left], height[right])
        max_water = max(max_water, width * h)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water

if __name__ == "__main__":
    print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
    print(maxArea([1, 1]))  # 1
    print(maxArea([4, 3, 2, 1, 4]))  # 16
    print(maxArea([1, 2, 1]))  # 2
