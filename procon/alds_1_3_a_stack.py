from collections import deque


def poland_calc(chars):
    stack = deque()
    for char in chars:
        if char == "+":
            res = stack.pop() + stack.pop()
            stack.append(res)
        elif char == "*":
            res = stack.pop() * stack.pop()
            stack.append(res)
        elif char == "-":
            res = - stack.pop() + stack.pop()
            stack.append(res)
        else:
            stack.append(int(char))
    return stack.pop()


def main():
    chars = input().split()
    print(poland_calc(chars))


if __name__ == "__main__":
    main()
