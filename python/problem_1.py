from typing import List


def distinct_difference_array(nums: List[int]) -> List[int]:
    result = []

    for i in range(len(nums)):
        prefix = len(set(nums[:i+1]))
        postfix = len(set(nums[i+1:]))

        difference = prefix - postfix

        result.append(difference)

    return result
