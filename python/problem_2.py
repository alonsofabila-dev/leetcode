from typing import List


def find_matrix(nums: List[int]) -> List[List[int]]:
    new_array = []
    nums_map = {}

    for num in nums:
        if num in nums_map:
            nums_map[num] += 1
        else:
            nums_map[num] = 1

    rows = max(nums_map.values())

    for row in range(rows):
        new_array.append([])

    for num, count in nums_map.items():
        for index in range(count):
            new_array[index].append(num)

    return new_array
