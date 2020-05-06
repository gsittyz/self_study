from collections import deque


class Process:
    def __init__(self, name, time):
        self.name = name
        self.time = int(time)


def main():
    n, q = map(int, input().split())
    queue = deque()
    for _ in range(n):
        name, time = input().split()
        queue.append(Process(name, time))

    time = 0
    while queue:
        process = queue.popleft()
        if process.time - q > 0:
            process.time -= q
            time += q
            queue.append(process)
        else:
            time += process.time
            print("{} {}".format(process.name, time))


if __name__ == "__main__":
    main()
