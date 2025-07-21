"""
Hour 1: Linear Search (Python + DSA)
Author: Ankith
Description: Implements linear search to find a target in a list.
"""

numbers = input("Enter numbers separated by spaces: ").split()
numbers = [int(num) for num in numbers]

target = int(input("Enter the number to search for: "))

found = False
for i in range(len(numbers)):
    if numbers[i] == target:
        print(f"Number is found at index {i}")
        found = True
        break

if not found:
    print("Number not found in the list.")
