import numpy as np
from collections import Counter
passage_name = [" "] + "1 2 3 4 5 6 7 8 9 0 A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split()


def print_space(space, max_i):
    for i in range(max_i):
        for j in range(10):
            print(passage_name[int(space[i][j])], end="")
        print("\n", end="")


def q4(filename):
    with open(filename) as f1:
        spaces = np.zeros((1000, 10))
        tiletxt = f1.readline()
        tiles = sorted([int(tile) for tile in tiletxt], reverse=True)
        # sorted_tiles = []
        # c = Counter(tiles)
        # while c[4] >= 1 and c[3] >= 2 and c[1] >= 2:
        #     sorted_tiles.extend([4, 3, 3, 1, 1])
        #     c.subtract({4: 1, 3: 2, 1: 2})
        # sorted_tiles.extend(sorted(c.elements()))
        # print(sorted_tiles)

        empty_count = np.array([10 for _ in range(1000)])
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
        print(i)

        # print_space(spaces, i)


if __name__ == "__main__":
    q4("./tile4a.txt")
    q4("./tile4b.txt")
    q4("./tile4c.txt")
