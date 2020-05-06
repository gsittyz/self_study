class Heap(list):
    def __init__(self, numbers=[]):
        super().__init__(numbers)

    def max_heapify(self, idx=0):
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

    def append(self, key):
        super().append(key)
        idx = len(self) - 1
        parent = (idx + 1) // 2 - 1
        while idx > 0 and self[parent] < self[idx]:  # 親のほうが小さい場合
            self[idx], self[parent] = self[parent], self[idx]
            idx = parent
            parent = (idx + 1) // 2 - 1

    def extract_max(self):
        max = self[0]
        if len(self) > 1:
            self[0] = self.pop()
            self.max_heapify()
        return max


def main():
    heap = Heap()
    while True:
        inputted = input()
        if inputted == "end":
            break
        elif inputted.startswith("insert"):
            heap.append(int(inputted.split()[1]))
        elif inputted == "extract":
            print(heap.extract_max())


if __name__ == "__main__":
    main()
