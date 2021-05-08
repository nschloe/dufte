import dufte


def assert_equality(a, b, eps):
    for x, y in zip(a, b):
        assert abs(x - y) < eps


def test_move_labels():
    out = dufte.main._move_min_distance([0.0, 1.0], 2.0)
    assert_equality(out, [-0.5, 1.5], 1.0e-5)

    out = dufte.main._move_min_distance([0.0, 1.0, 3.0], 2.0)
    assert_equality(out, [-2 / 3, 4 / 3, 10 / 3], 1.0e-5)

    out = dufte.main._move_min_distance([0.0, 0.0, 3.0], 2.0)
    assert_equality(out, [-1.0, 1.0, 3.0], 1.0e-5)
