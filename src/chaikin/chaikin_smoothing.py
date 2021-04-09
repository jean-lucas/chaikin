import numpy as np
from more_itertools import windowed

openLine = [[0,0], [0, 1], [1, 1], [1.5, -0.5], [3, 2], [3,3]]
closed = [[0,0], [0, 1], [1,1.5], [1, 0], [0, 0]]


def _smooth(a) -> np.array:
    new_pts = []
    for w in windowed(a, 2):
        q = 0.75 * w[0] + 0.25 * w[1]
        r = 0.25 * w[0] + 0.75 * w[1]
        new_pts.extend([q, r])
    return np.array(new_pts)


def smooth(a: np.array, n: 2) -> np.array:
    smoothed_pts = a
    for _ in range(n):
        smoothed_pts = _smooth(smoothed_pts)
