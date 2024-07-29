import python.problem_2 as problem


def test_same_nums():
    """
    Test case where nums contains some repeated numbers.
    """
    # Arrange
    nums = [1, 3, 4, 1, 2, 3, 1]
    expected_result = [[1, 3, 4, 2], [1, 3], [1]]

    # Act
    result = problem.find_matrix(nums)

    # Assert
    assert result == expected_result


def test_all_distinct_nums():
    """
    Test case where nums contains all distinct numbers.
    """
    # Arrange
    nums = [1, 2, 3, 4]
    expected_result = [[1, 2, 3, 4]]

    # Act
    result = problem.find_matrix(nums)

    # Assert
    assert result == expected_result
