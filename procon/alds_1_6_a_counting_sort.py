def counting_sort(in_arr, out_arr, arr_len, max_val):
    counter = [0] * (max_val + 1)  # 0, 1, 2, 3, ..., max_valのカウンター

    for i in range(arr_len):
        counter[in_arr[i]] += 1  # counterに出現数を記録

    for j in range(max_val):
        counter[j + 1] = counter[j + 1] + counter[j]  # 累積わ

    for i in reversed(range(0, arr_len)):  # 係数ソートは後ろから選んでいくと安定
        out_arr[counter[in_arr[i]] - 1] = in_arr[i]  # out_arrはindex, counterは個数なので1挽く
        counter[in_arr[i]] -= 1


def main():
    n = int(input())
    in_arr = list(map(int, input().split(" ")))
    out_arr = [0] * n
    counting_sort(in_arr, out_arr, n, 10000)
    print(" ".join(map(str, out_arr)))


if __name__ == "__main__":
    main()
