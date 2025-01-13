from pascal_triangle import triangle_row


def test_row_0():
    assert triangle_row(0) == [1]


def test_row_1():
    assert triangle_row(1) == [1, 1]


def test_row_2():
    assert triangle_row(2) == [1, 2, 1]


def test_row_3():
    assert triangle_row(3) == [1, 3, 3, 1]


def test_row_4():
    assert triangle_row(4) == [1, 4, 6, 4, 1]
