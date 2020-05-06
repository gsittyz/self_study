# def f(n):
#     if n < 1:
#         return 1
#     else:
#         return (161 * f(n - 1) + 2457) % (2**24)


def f(n):
    res = 1
    for _ in range(n):
        res = (161 * res + 2457) % (2**24)
    return res


print(f(10))


def f_count_even(n):
    res = 1
    count = 0
    for _ in range(n):
        res = (161 * res + 2457) % (2**24)
        if (res % 2 == 0):
            count += 1
    return count


print(f_count_even(99))


def f_count_even_even(n):
    res = 1
    count = 0
    for i in range(n):
        res = (161 * res + 2457) % (2**24)
        if (i % 2 == 0 and res % 2 == 0):
            count += 1
    return count


print(f_count_even_even(99))

print(f(1000000))


def g(n):
    res = 1
    for _ in range(n):
        res = (1103515245 * res + 12345) % (2**26)
    return res


print(g(2))
print(g(3))


def gnkg(n):
    gn = g(n)
    k = 1
    gnk = (1103515245 * gn + 12345) % (2**26)
    while gn != gnk:
        k += 1
        gnk = (1103515245 * gnk + 12345) % (2**26)
    return k


def hnkh(n):
    gn = g(n)
    hn = gn % (2**10)
    k = 1
    gnk = (1103515245 * gn + 12345) % (2**26)
    hnk = gnk % (2**10)
    while hn != hnk:
        k += 1
        gnk = (1103515245 * gnk + 12345) % (2**26)
        hnk = gnk % (2**10)
    return k


print(hnkh(1))
