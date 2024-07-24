import python.problem_1 as problems


def test_different_numbers():
    nums = [1, 2, 3, 4, 5]
    expected_result = [-3, -1, 1, 3, 5]

    result = problems.distinct_difference_array(nums)

    assert result == expected_result


def test_list_with_same_numbers():
    nums = [3, 2, 3, 4, 2]
    expected_result = [-2, -1, 0, 2, 3]

    result = problems.distinct_difference_array(nums)

    assert result == expected_result
