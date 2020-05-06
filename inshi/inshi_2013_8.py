import numpy as np


def q1(d):
    d = abs(d)
    return int((10 // d + 1) ** 2)


def q2(d):
    d = abs(d)

    A0 = q1(d)
    A1 = 0
    p = 0
    q = 0
    while d * p <= 10:
        q = 0
        while d * q <= 10:
            if (d * p - 5) ** 2 + (d * q - 5) ** 2 <= 25:
                A1 += 1
            q += 1
        p += 1
    print(A1)
    return A1 / A0 / 4


def koch_points(n, points=[np.array([0, 0]), np.array([10, 0]), np.array([5, 5 * (3**0.5)])]):
    def koch(start, end, depth, rotmat):
        if depth == 0:
            return []
        next1 = (start * 2 + end * 1) / 3
        next2 = (start * 1 + end * 2) / 3
        koch_point = (start - next1) @ rotmat.T + next1

        return koch(start,
                    next1,
                    depth - 1,
                    rotmat) + [next1] + koch(next1,
                                             koch_point,
                                             depth - 1,
                                             rotmat) + [koch_point] + koch(koch_point,
                                                                           next2,
                                                                           depth - 1,
                                                                           rotmat) + [next2] + koch(next2,
                                                                                                    end,
                                                                                                    depth - 1,
                                                                                                    rotmat)
    rotmat = np.array([[np.cos(2 * np.pi / 3), - np.sin(2 * np.pi / 3)],
                       [np.sin(2 * np.pi / 3), np.cos(2 * np.pi / 3)]])
    return [points[0]] + [koch(points[0], points[1], n, rotmat)] +\
        [points[1]] + [koch(points[1], points[2], n, rotmat)] + [points[2]]


def q4(n):
    triangle = 25 * (3**0.5)
    edges = 3
    area = triangle
    for _ in range(n):
        triangle = triangle / 9
        area += triangle * edges
        edges = edges * 4
    return area


def q6(d, n):
    ks = koch_points(n)
