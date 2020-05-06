# def linear_search(seq1, seq2):
#     count = 0
#     for i in seq1:
#         for j in seq2:
#             if i == j:
#                 count += 1
#     return count


def binary_search(seq, seq1_len, key):
    left = 0
    right = seq1_len
    center = 0
    while left < right:
        center = (left + right) // 2
        if seq[center] == key:
            return True
        if key < seq[center]:
            right = center
        else:
            left = center + 1
    return False


def main():
    # num_seq1 = int(input())
    seq1_len = int(input())
    seq1 = list(map(int, input().split(" "))) + [0]  # 番兵
    # num_seq2 = int(input())
    input()
    seq2 = list(map(int, input().split(" ")))
    count = 0
    for key in seq2:
        if binary_search(seq1, seq1_len, key):
            count += 1

    print(count)


if __name__ == "__main__":
    main()
