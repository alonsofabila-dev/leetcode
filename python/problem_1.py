from typing import List


def distinct_difference_array(nums: List[int]) -> List[int]:
    """
    Function to find the distinct difference array.

    Args:
        nums: (List[int], required): List of integers

    Returns:
    List of integers representing the distinct difference array
    """
    result = []

    for i in range(len(nums)):
        # Calculate the number of distinct elements in the prefix.
        prefix = len(set(nums[:i+1]))
        # Calculate the number of distinct elements in the suffix.
        postfix = len(set(nums[i+1:]))

        difference = prefix - postfix

        result.append(difference)

    return result
