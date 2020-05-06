def greatest_common_divisor(a, b):
    # a 割る b = c あまり d
    # b 割る d = ...
    residue = a % b
    if residue != 0:
        return greatest_common_divisor(b, residue)
    return b


def main():
    a, b = map(int, input().split(" "))
    print(greatest_common_divisor(a, b))


if __name__ == "__main__":
    main()
