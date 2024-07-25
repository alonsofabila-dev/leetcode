import python.problem_2 as problem


def test_same_nums():
    nums = [1, 3, 4, 1, 2, 3, 1]
    expected_result = [[1, 3, 4, 2], [1, 3], [1]]

    result = problem.find_matrix(nums)

    assert result == expected_result


def test_all_distinct_nums():
    nums = [1, 2, 3, 4]
    expected_result = [[1, 2, 3, 4]]

    result = problem.find_matrix(nums)

    assert result == expected_result
