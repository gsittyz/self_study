a, b = input().split()
ab = a * int(b)
ba = b * int(a)
i = 0
while i < len(ab) and i < len(ba):
    if ab[i] == ba[i]:
        i += 1
        continue
    elif int(ab[i]) < int(ba[i]):
        print(ab)
        break
    else:
        print(ba)
        break
if i == len(ab):
    print(ab)
elif i == len(ba):
    print(ba)
