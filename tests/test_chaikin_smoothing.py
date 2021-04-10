import numpy as np
from chaikin.chaikin_smoothing import smooth

openLine = [[0, 0], [0, 1], [1, 1], [1.5, -0.5], [3, 2], [3,3]]
closed = [[0, 0], [0, 1], [1,1.5], [1, 0], [0, 0]]
simple_line = [[1, 1], [2, 2]]


def test_open_line_smooth():
    expected_pts = [[1.25, 1.25], [1.75, 1.75]]
    actual_pts = smooth(simple_line, n=1)
    np.testing.assert_array_equal(actual_pts, expected_pts)
