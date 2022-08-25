from code_challenges.quick_sort import quick_sort


def test_quick_sort():
    list = [1,4,2,9]
    actual = quick_sort(list)
    expected = [1,2,4,9]
    assert actual == expected
