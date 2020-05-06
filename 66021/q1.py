from collections import deque


def q1():
    with open("./tile1.txt") as f1:
        tiles = f1.readline()
        spaces = deque([])
        depth = 0
        for tile in tiles:
            i = int(tile)
            if i == 1:
                if len(spaces) == 0:
                    depth += i
                    spaces.append(depth)
                else:
                    spaces.popleft()
            elif i == 2:  # elseでもいい
                depth += i
        print(depth)


q1()
# def q2():


#         spaces = []
#         width = 0
#         depth = 0
#         for tile in tiles:
#             i = int(tile)
#             if len(spaces) == 0:
#                 if width == 0:
#                     spaces.append((depth, width - i, float("inf")))
#                     depth += i


#             if width == 0:
#                 depth += i
#                 width = 2 - i
#             elif width == 1:
#                 if i == 1:
#                     # depthは何もしない
