def search(t, p):
    tn = len(t)
    i = 0
    pn = len(p)
    plist = []
    if pn <= tn:
        while i < tn:
            j = 0
            while j < pn and i + j < tn:
                if t[i + j] != p[j]:
                    break
                j += 1
            if j == pn:
                plist.append(i)
            i += 1
    return plist


def main():
    t = input()
    p = input()
    plist = search(t, p)
    for i in plist:
        print(i)


if __name__ == "__main__":
    main()
