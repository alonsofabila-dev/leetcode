from typing import List


def permute(nums: List[int]) -> List[List[int]]:

    if len(nums) == 0:
        return [[]]

    permutations = permute(nums[1:])
    result = []

    for permutation in permutations:
        for index in range(len(permutation) + 1):
            copy = permutation.copy()
            copy.insert(index, nums[0])
            result.append(copy)

    return result
