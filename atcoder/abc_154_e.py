from operator import mul
from functools import reduce
nstr = input()
t = len(nstr)
n = int(nstr)
k = int(input())


def com(n, r):
    r = min(r, n - r)
    numer = reduce(mul, range(n, n - r, -1), 1)
    denom = reduce(mul, range(1, r + 1), 1)
    return numer // denom


def kosu(n, t, k):
    top = n // (10 ** (t - 1))
    nextn = n % (10 ** (t - 1))
    if t == 1:
        return n
    else:
        return kosu(nextn, t - 1, k - 1) + (top - 1) * (9 ** (k - 1)) * \
            com(t - 1, k - 1) + (9 ** k) * com(t - 1, k)


print(kosu(n, t, k))


"""
0でない数字k個
t ... nの桁数
k桁 0以外k桁
k + 1 桁 0以外1桁 + k桁中0が1桁
k + 2 桁 0以外1桁 + k+1桁中0が2桁
k + 3 桁 0以外1桁 + k+2桁中0が3桁
……
t - 1 桁 0以外1桁 + t-2桁中0がt-1-k桁
t 桁 1以上a以下1桁 + t-1桁中0がt-1-k桁
a (それ以下の整数であって0でない数字がちょうどK-1個ある)
1〜a-1 9通り ** k - 1 桁　× t - 1 C k - 1
0 (9通り ** k桁)　× t - 1 C k
"""
