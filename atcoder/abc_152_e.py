import sys
sys.setrecursionlimit(99999)
n = int(input())
# ns = list(map(int, input().split()))
ns = list(range(1, n))


def gcd(a, b):
    if (b == 0):
        return a
    return gcd(b, a % b)


def lcm(ns):
    if len(ns) == 1:
        return ns[0]
    elif len(ns) == 2:
        return ns[0] * ns[1] / gcd(ns[0], ns[1])
    else:
        mid = len(ns) // 2
        return lcm([lcm(ns[:mid]), lcm(ns[mid:])])


l = lcm(ns)
s = 0
for i in ns:
    s += l / i
    s %= 10**9 + 7
print(int(s))
