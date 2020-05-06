from heapq import heappop, heappush
# 4
with open("./inshi/image2.txt") as f1:
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
    pixnum = len_col * len_row
    heap = []
    for i in range(len_col * len_row):
        column = i % len_col
        row = i // len_col
        brightness = sum([image[row][column][i] ** 2 for i in range(3)])
        heappush(heap, (brightness, i, image[row][column]))

    idxs = [pixnum * i / 4 for i in range(4)]
    for time in range(pixnum):
        brightness, i, pix = heappop(heap)
        if time in idxs:
            print(pix, i)
