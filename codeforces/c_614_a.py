t = int(input())
for _ in range(t):
    n, s, k = list(map(int, input().split()))
    closed = list(map(int, input().split()))
    is_open = []
    for i in range(n):
        is_open.append(True)
    for i in closed:
        is_open[i - 1] = False
    upper = s
    lower = s - 1
    while upper <= n or 1 <= lower:
        if upper <= n:
            if is_open[upper - 1]:
                print(upper - s)
                break
            else:
                upper += 1
        if 1 <= lower:
            if is_open[lower - 1]:
                print(s - lower)
                break
            else:
                lower -= 1
