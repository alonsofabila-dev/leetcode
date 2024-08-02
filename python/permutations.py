from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    """
    Function to generate all possible permutations.

    Args:
        nums: (List[int], required): List of integers

    Returns:
    A list of all possible permutations.
    """
    if len(nums) == 0:
        return [[]]

    # Recursively call permute on the list excluding the first element
    permutations = permute(nums[1:])
    result = []

    # Iterate over each permutation returned by the recursive call
    for permutation in permutations:
        # Insert the first element of the original list into every possible position
        for index in range(len(permutation) + 1):
            # Make a copy of the current permutation
            copy = permutation.copy()
            # Insert the first element at the current position
            copy.insert(index, nums[0])
            result.append(copy)

    return result
