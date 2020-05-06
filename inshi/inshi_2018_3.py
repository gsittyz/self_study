from heapq import heapify, heappop, heappush
# 3
with open("./inshi/image1.txt") as f1:
    lines = f1.readlines()
    image = []

    for line in lines:
        split = line.rstrip().split()
        split = list(map(int, split))
        row = []
        for i in range(0, len(split), 3):
            row.append(split[i:i + 3])
        image.append(row)
    print(image)
    len_row = len(image)
    len_col = len(image[0])
    # (3)
    heap = []
    for i in range(len_col * len_row):
        column = i % len_col
        row = i // len_col
        brightness = sum([image[row][column][i] ** 2 for i in range(3)])
        heappush(heap, (brightness, i, image[row][column]))

    for time in range(len_col * len_row // 2 + 1):
        brightness, i, pix = heappop(heap)
        if time == len_col * len_row / 2:
            print(pix, i)
