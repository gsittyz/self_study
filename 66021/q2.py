import numpy as np


def q2(filename):
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
        print(i)


if __name__ == "__main__":
    q2("./tile2a.txt")
    q2("./tile2b.txt")
    q2("./tile2c.txt")
    # q2("./tile2d.txt")
