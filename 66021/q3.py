import numpy as np
passage_name = [" "] + "1 2 3 4 5 6 7 8 9 0 A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split()


def print_space(space, max_i):
    for i in range(max_i):
        for j in range(10):
            print(passage_name[int(space[i][j])], end="")
        print("\n", end="")


def q3(filename):
    with open(filename) as f1:
        spaces = np.zeros((1000, 10))
        # depth = [0] * 10
        tiletxt = f1.readline()
        empty_count = np.array([10 for _ in range(1000)])
        tiles = [int(tile) for tile in tiletxt]
        for no, tile in enumerate(tiles):
            i = 0
            j = 0
            while True:
                if i >= 1000 - tile:
                    break
                elif empty_count[i] < tile:
                    i += 1
                elif j > 10 - tile:
                    i += 1
                    j = 0
                elif spaces[i:i + tile, j:j + tile].sum() > 0:
                    j += 1
                else:
                    break
            if i < 1000 - tile:
                spaces[i:i + tile, j:j + tile] = no + 1
                empty_count[i:i + tile] = empty_count[i:i + tile] - tile

        while spaces[i].sum() > 0:
            i += 1

        print_space(spaces, i)


# def q3(filename):
#     with open(filename) as f1:
#         spaces = np.zeros((1000, 10))
#         tiletxt = f1.readline()
#         tiles = [int(tile) for tile in tiletxt]
#         for no, tile in enumerate(tiles):
#             i = 0
#             j = 0
#             while True:
#                 if i >= 1000 - tile:
#                     break
#                 elif j > 10 - tile:
#                     i += 1
#                     j = 0
#                 elif spaces[i:i + tile, j:j + tile].sum() > 0:
#                     j += 1
#                 else:
#                     break
#             if i < 1000 - tile:
#                 spaces[i:i + tile, j:j + tile] = no + 1

#         while spaces[i].sum() > 0:
#             i += 1
#         print_space(spaces, i)


if __name__ == "__main__":
    print("--------title3a-----------")
    q3("./tile3a.txt")
    # q2("./tile3a.txt")
    print()
    print("--------title3b-----------")
    q3("./tile3b.txt")
    print()
    print("-------title3c-----------")
    q3("./tile3c.txt")
