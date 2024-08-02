import python.distinct_difference_array as problems


def test_different_numbers():
    """
    Test the distinct_difference_array function with a list of different numbers.
    """
    # Arrange
    nums = [1, 2, 3, 4, 5]
    expected_result = [-3, -1, 1, 3, 5]

    # Act
    result = problems.distinct_difference_array(nums)

    # Assert
    assert result == expected_result


def test_list_with_same_numbers():
    """
    Test the distinct_difference_array function with a list containing some repeated numbers.
    """
    # Arrange
    nums = [3, 2, 3, 4, 2]
    expected_result = [-2, -1, 0, 2, 3]

    # Act
    result = problems.distinct_difference_array(nums)

    # Assert
    assert result == expected_result
