from typing import List


def find_matrix(nums: List[int]) -> List[List[int]]:
    """
    Function to find the matrix of distinct numbers.

    Args:
        nums: (List[int], required): List of integers

    Returns:
    A 2D array where each row contains distinct integers and the number of rows is minimal.
    """
    new_array = []
    nums_map = {}

    # Count the occurrences of each number in nums
    for num in nums:
        if num in nums_map:
            nums_map[num] += 1
        else:
            nums_map[num] = 1

    # Determine the number of rows needed, which is the maximum count of any number
    rows = max(nums_map.values())

    # Initialize the 2D array
    for row in range(rows):
        new_array.append([])

    # Distribute the numbers into the 2D array
    for num, count in nums_map.items():
        for index in range(count):
            new_array[index].append(num)

    return new_array
