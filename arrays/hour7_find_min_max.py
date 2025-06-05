"""
Hour 7: Find Minimum and Maximum (Python + DSA)
Author: Ankith
Description: Finds the smallest and largest values in a user-entered list.
"""

numbers = input("Enter numbers separated with spaces: ").split()

# Handle empty input
if not numbers or all(num.strip() == '' for num in numbers):
    print("No numbers entered. Please enter at least one number.")
else:
    numbers = [int(num) for num in numbers]

    minimum = numbers[0]
    maximum = numbers[0]

    for num in numbers:
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num

    print(f"Minimum: {minimum}")
    print(f"Maximum: {maximum}")
