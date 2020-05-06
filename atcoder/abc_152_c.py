n = int(input())
ns = list(map(int, input().split()))
min_n = float("inf")
count = 0
for i in ns:
    if i < min_n:
        count += 1
        min_n = i
    if i == 1:
        break
print(count)
