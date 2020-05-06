# AIJではnumpyはつかえない

import numpy as np

rotation_matrix = np.array([[np.cos(np.pi / 3), -np.sin(np.pi / 3)],
                            [np.sin(np.pi / 3), np.cos(np.pi / 3)]])


def koch_curve(p1, p2, depth):
    s = (p1 * 2 + p2) / 3
    t = (p1 + p2 * 2) / 3
    u = np.matmul(t - s, rotation_matrix.T) + s
    if depth > 1:
        koch_curve(p1, s, depth - 1)
    print("{} {}".format(s[0], s[1]))
    if depth > 1:
        koch_curve(s, u, depth - 1)
    print("{} {}".format(u[0], u[1]))
    if depth > 1:
        koch_curve(u, t, depth - 1)
    print("{} {}".format(t[0], t[1]))
    if depth > 1:
        koch_curve(t, p2, depth - 1)


def main():
    depth = int(input())
    p1 = np.array([0.0, 0.0])
    p2 = np.array([100.0, 0.0])
    print("{} {}".format(p1[0], p1[1]))
    koch_curve(p1, p2, depth)
    print("{} {}".format(p2[0], p2[1]))


if __name__ == "__main__":
    main()
