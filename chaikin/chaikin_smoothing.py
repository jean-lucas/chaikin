import numpy as np
from more_itertools import windowed


def _smooth(a: np.array) -> np.array:
    new_pts = []
    print(a)
    for w in windowed(a, 2):
        q = (0.75 * w[0]) + (0.25 * w[1])
        r = (0.25 * w[0]) + (0.75 * w[1])
        print(w, q, r)
        new_pts.extend([q, r])
    return np.array(new_pts)


def smooth(a: np.array, n: int = 2) -> np.array:
    """
    Smooth a two dimensional array of coordinates using hte Chaikin method as specified
    here: http://www.idav.ucdavis.edu/education/CAGDNotes/Chaikins-Algorithm/Chaikins-Algorithm.html

    Args:
        a: two dimensional input array
        n: number of iterations, defaults to 2
    Returns:
        A smoothed out 2d numpy array
    """
    invalid_input_msg = f"Input must be a 2-d list or numpy array, but got: {a}"
    if not isinstance(a, np.ndarray):
        try:
            a = np.array(a)
        except:
            raise Exception(invalid_input_msg)

    if not len(a.shape) == 2 and a.shape[1] != 2:
        raise Exception(f"Input must be a 2-d array")

    smoothed_pts = a
    for _ in range(n):
        print("a", smoothed_pts)
        smoothed_pts = _smooth(smoothed_pts)

    return smoothed_pts
