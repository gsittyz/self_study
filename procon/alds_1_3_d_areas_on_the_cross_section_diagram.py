from collections import deque


def calc_area(chars):
    s1 = deque()
    s2 = deque()
    area = 0

    for idx, char in enumerate(chars):
        if char == "\\":
            s1.append(idx)
        elif char == "/":
            if s1:
                left_idx = s1.pop()
                sub_area = idx - left_idx
                area = area + sub_area
                while s2 and left_idx < s2[-1][0]:
                    sub_area += s2.pop()[1]
                s2.append((left_idx, sub_area))
    return area, s2


def main():
    chars = input()
    area, s2 = calc_area(chars)
    print(area)
    text = ""
    count = 0
    while s2:
        text += " " + str(s2.popleft()[1])
        count += 1
    print(str(count) + text)


if __name__ == "__main__":
    main()
