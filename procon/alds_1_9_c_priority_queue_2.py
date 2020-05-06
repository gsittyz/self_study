from heapq import heapify, heappop, heappush


def main():
    heap = []
    while True:
        operation = input()
        if operation[0] == "i":
            heappush(heap, -int(operation.split()[1]))
        elif operation[1] == "x":
            print(-heappop(heap))
        else:
            break


if __name__ == "__main__":
    main()
