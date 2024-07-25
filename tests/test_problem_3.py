import python.problem_3 as problem


def test_three_element_permutation():
    nums = [1, 2, 3]
    expected_result = [[1, 2, 3], [2, 1, 3], [2, 3, 1], [1, 3, 2], [3, 1, 2], [3, 2, 1]]

    result = problem.permute(nums)

    assert result == expected_result


def test_one_element_permutation():
    nums = [1]
    expected_result = [[1]]

    result = problem.permute(nums)

    assert result == expected_result
