from collections import deque


def shell_sort(arr, n):
    def insertion_sort(arr, n, dist):
        nonlocal cnt
        for right_idx in range(dist, n):
            right_val = arr[right_idx]
            left_idx = right_idx - dist
            while left_idx >= 0 and arr[left_idx] > right_val:
                arr[left_idx + dist] = arr[left_idx]
                left_idx -= dist
                cnt += 1
            arr[left_idx + dist] = right_val
    cnt = 0
    dists = deque()
    dist = 1
    while dist <= n:
        dists.appendleft(dist)
        dist = dist * 3 + 1
    dists = list(dists)
    m = len(dists)

    for i in range(m):
        insertion_sort(arr, n, dists[i])

    return m, dists, cnt


def main():
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    m, dists, cnt = shell_sort(arr, n)
    print(m)
    print(" ".join(list(map(str, dists))))
    print(cnt)
    for i in arr:
        print(i)


if __name__ == "__main__":
    main()
