class Card():
    def __init__(self, num, mark):
        self.num = num
        self.mark = mark

    def __eq__(self, other):
        if other is None or not isinstance(other, Card):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self.__eq__(other)


def partition(array, start, end):
    end_val = array[end].num
    left_end = start - 1
    for search_idx in range(start, end):
        if array[search_idx].num <= end_val:
            left_end += 1
            array[left_end], array[search_idx] = array[search_idx], array[left_end]
    array[left_end + 1], array[end] = array[end], array[left_end + 1]
    return left_end + 1


def quicksort(array, start, end):
    if start < end:
        pivot_index = partition(array, start, end)
        quicksort(array, start, pivot_index - 1)
        quicksort(array, pivot_index + 1, end)


def mergesort(array, n):
    if n <= 1:
        return array
    left_end = n // 2
    left_sorted = mergesort(array[:left_end], left_end) + [Card(10**9, None)]
    right_sorted = mergesort(array[left_end:], n - left_end) + [Card(10**9, None)]
    left_idx, right_idx = 0, 0
    idx = 0
    sorted_list = [None] * n
    while idx < n:
        if left_sorted[left_idx].num <= right_sorted[right_idx].num:
            sorted_list[idx] = left_sorted[left_idx]
            left_idx += 1
        else:
            sorted_list[idx] = right_sorted[right_idx]
            right_idx += 1
        idx += 1
    return sorted_list


def main():
    n = int(input())
    cards = []
    for _ in range(n):
        mark, number = input().split(" ")
        cards.append(Card(int(number), mark))
    mergesorted_cards = mergesort(cards, n)
    quicksort(cards, 0, n - 1)
    message = "Stable"
    for i in range(n):
        if mergesorted_cards[i] != cards[i]:
            message = "Not stable"
    print(message)
    for i in range(n):
        print("{} {}".format(cards[i].mark, cards[i].num))


if __name__ == "__main__":
    main()
