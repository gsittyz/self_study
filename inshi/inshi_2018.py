# q2
import numpy as np


def q2():
    with open("mat1.txt") as f1:
        matstr = f1.readline().rstrip().rstrip(".")
        rows = matstr.split(",")
        print(len(rows))
        print(len(rows[0].split()))


# q3


def conv2mat(filepath):
    with open(filepath) as f1:
        matstr = f1.readline().rstrip().rstrip(".")
        rows = matstr.split(",")
        mat = [list(map(int, row.split())) for row in rows]
        return mat


def q3():
    mat1 = np.array(conv2mat("mat1.txt"))
    mat2 = np.array(conv2mat("mat2.txt"))
    res = mat1 @ mat2
    s = 0
    for i in range(len(res)):
        s += res[i][i]
    print(s)


def q4(m, n, s):
    from collections import deque
    cache = deque([])
    a = [[False for _ in range(n)] for _ in range(m)]
    b = [[False for _ in range(m)] for _ in range(n)]
    ab = [a, b]
    i = 0
    count = 0
    while i < m:
        j = 0
        while j < m:
            k = 0
            while k < n:
                if not a[i][k]:
                    count += 1
                    if len(cache) == s:
                        lru = cache.popleft()
                        ab[lru[0]][lru[1]][lru[2]] = False
                    cache.append([0, i, k])
                    a[i][k] = True
                if not b[k][j]:
                    count += 1
                    if len(cache) == s:
                        lru = cache.popleft()
                        ab[lru[0]][lru[1]][lru[2]] = False
                    cache.append([1, k, j])
                    b[k][j] = True
                k = k + 1
            j = j + 1
        i = i + 1
    return count


print(q4(12, 24, 40))


def q5(m, n, s, p):
    from collections import deque
    cache = deque([])
    a = [[False for _ in range(n)] for _ in range(m)]
    b = [[False for _ in range(m)] for _ in range(n)]
    ab = [a, b]
    u = 0
    count = 0
    while u < m:
        v = 0
        while v < m:
            w = 0
            while w < n:
                i = u
                while i < u + p:
                    j = v
                    while j < v + p:
                        k = w
                        while k < w + p:
                            if not a[i][k]:
                                count += 1
                                if len(cache) == s:
                                    lru = cache.popleft()
                                    ab[lru[0]][lru[1]][lru[2]] = False
                                cache.append([0, i, k])
                                a[i][k] = True
                            if not b[k][j]:
                                count += 1
                                if len(cache) == s:
                                    lru = cache.popleft()
                                    ab[lru[0]][lru[1]][lru[2]] = False
                                cache.append([1, k, j])
                                b[k][j] = True
                            k = k + 1
                        j = j + 1
                    i = i + 1
                w = w + p
            v = v + p
        u = u + p
    return count


def q5(m, n, s):
    import math
    p = math.gcd(m, n)
    # エラトステネスの篩
    prt = int(p ** 0.5)
    numlis = list(range(2, prt + 1))
    j = 0
    while j < len(numlis):
        prime = numlis[j]
        i = 1
        while prime * i < prt:
            numlis.remove(prime * i)
            i += 1
        j = j + 1
    # 素数


print(q5(12, 24, 40, 12))
