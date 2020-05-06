def bubble_sort(arr, n):
    for i in range(n):
        for j in reversed(range(i + 1, n)):
            if arr[j - 1].value > arr[j].value:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
    return arr


def selection_sort(arr, n):
    for i in range(n):
        min_idx = i
        for j in range(i, n):
            if arr[j].value < arr[min_idx].value:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


class Card:
    def __init__(self, card_str):
        self.value = int(card_str[1])
        self.mark = card_str[0]
        self.str = card_str


def is_stable(stable_arr, target_arr):
    for s, t in zip(stable_arr, target_arr):
        if s.str != t.str:
            return False
    return True


def main():
    n = int(input())
    # cards = ["H4", "C9", "S4", "D2", "C3"]
    cards = input().split()
    arr = [Card(card_str) for card_str in cards]
    # n = 5
    b_arr = bubble_sort(arr, n)
    print(" ".join([b.str for b in b_arr]))
    print("Stable")
    arr = [Card(card_str) for card_str in cards]
    s_arr = selection_sort(arr, n)
    print(" ".join([s.str for s in s_arr]))
    if is_stable(b_arr, s_arr):
        print("Stable")
    else:
        print("Not stable")


if __name__ == "__main__":
    main()
