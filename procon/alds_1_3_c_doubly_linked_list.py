from collections import deque


def main():
    n = int(input())
    dll = deque()

    def delete(x):
        try:
            dll.remove(x)
        except ValueError:
            pass

    methods = {"insert": dll.appendleft,
               "delete": delete,
               "deleteFirst": dll.popleft,
               "deleteLast": dll.pop}
    for _ in range(n):
        command = input().split()
        if len(command) > 1:
            methods[command[0]](int(command[1]))
        else:
            methods[command[0]]()
        # print(dll)

    print(" ".join(map(str, dll)))


if __name__ == "__main__":
    main()
