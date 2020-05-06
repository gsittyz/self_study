def floyd(dismat, v):
    for k in range(v):
        for i in range(v):
            if dismat[i][k] != float("inf"):
                for j in range(v):
                    if dismat[k][j] != float("inf"):
                        dismat[i][j] = min(dismat[i][j], dismat[i][k] + dismat[k][j])
    return dismat


def main():
    ve = input().split()
    v, e = tuple(map(int, ve))
    dismat = [[float("inf") for _ in range(v)] for _ in range(v)]
    for _ in range(e):
        std = input().split()
        s, t, d = tuple(map(int, std))
        dismat[s][t] = d
    for i in range(v):
        dismat[i][i] = 0
    dismat = floyd(dismat, v)
    for i in range(v):
        if dismat[i][i] < 0:
            print("NEGATIVE CYCLE")
            return
    for i in range(v):
        for j in range(v):
            if dismat[i][j] == float("inf"):
                dismat[i][j] = "INF"
        print(" ".join(map(str, dismat[i])))


if __name__ == "__main__":
    main()
