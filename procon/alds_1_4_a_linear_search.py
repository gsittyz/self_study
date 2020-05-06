# def linear_search(seq1, seq2):
#     count = 0
#     for i in seq1:
#         for j in seq2:
#             if i == j:
#                 count += 1
#     return count
from copy import deepcopy


def linear_search(seq, seq1_len, key):
    # 番兵
    seq[seq1_len] = key
    i = 0
    while seq[i] != key:
        i += 1
    return i != seq1_len


def main():
    # num_seq1 = int(input())
    seq1_len = int(input())
    seq1 = list(map(int, input().split(" "))) + [0]  # 番兵
    # num_seq2 = int(input())
    input()
    seq2 = list(map(int, input().split(" ")))
    count = 0
    for key in seq2:
        if linear_search(seq1, seq1_len, key):
            count += 1

    print(count)


if __name__ == "__main__":
    main()
