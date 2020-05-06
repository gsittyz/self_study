n = int(input())
xs = list(map(int, input().split()))
p = round(sum(xs) / n)
print(sum([(x - p)**2 for x in xs]))
