def modpow(x, n, mod):
    res = 1
    while (n > 0):
        if (n & 1):
            res *= x
            res %= mod
        x *= x
        x %= mod
        n >>= 1
    return res


def comb(a, b, p):
    if (b > a - b):
        return comb(a, a - b, p)
    c = d = 1
    for i in range(b):
        c *= (a - i)
        d *= (b - i)
        c %= p
        d %= p
    return c * modpow(d, p - 2, p) % p


n, a, b = map(int, input().split())
mod = 10**9 + 7
all = modpow(2, n, mod)
res = (all - 1 - comb(n, a, mod) - comb(n, b, mod)) % mod
print(res)
