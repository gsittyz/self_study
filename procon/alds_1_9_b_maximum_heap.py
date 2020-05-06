class Heap(list):
    def __init__(self, numbers=[]):
        super().__init__(numbers)

    def max_heapify(self, idx):
        left = (idx + 1) * 2 - 1
        right = (idx + 1) * 2 + 1 - 1

        if left < len(self) and self[left] > self[idx]:
            largest = left
        else:
            largest = idx
        if right < len(self) and self[right] > self[largest]:
            largest = right

        if largest != idx:
            self[idx], self[largest] = self[largest], self[idx]
            self.max_heapify(largest)

    def build_max_heap(self):
        for i in range(len(self) // 2, 0, -1):
            self.max_heapify(i - 1)


def main():
    n = int(input())
    nums = list(map(int, input().split()))
    heap = Heap(nums)
    heap.build_max_heap()
    for i in range(n):
        print(" {}".format(heap[i]), end="")
    print("\n", end="")


if __name__ == "__main__":
    main()
