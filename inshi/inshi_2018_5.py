from heapq import heappop, heappush
# 6
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
    k = 4
    idxs = [pixnum * i / k for i in range(k)]
    colors = []
    assign = [0] * pixnum
    num = [0] * k
    # 代表画素の初期値
    for time in range(pixnum):
        brightness, i, pix = heappop(heap)
        if time in idxs:
            colors.append(pix)
    # Cluster分類
    for time in range(pixnum):
        column = time % len_col
        row = time // len_col
        r, g, b = image[row][column]
        min_dist = float("inf")
        min_idx = 0
        for i in range(k):
            rc, gc, bc = colors[k]
            dist = abs(r - rc) + abs(g - gc) + abs(b - bc)
            if dist <= min_dist:
                min_dist = dist
                min_idx = i
        assign[time] = min_idx
        num[min_idx] += 1
    for _ in range(10):
        # 中心点を求める
        new_color = [[0, 0, 0] for i in range(k)]
        for time in range(pixnum):
            column = time % len_col
            row = time // len_col
            r, g, b = image[row][column]
            assign_idx = assign[time]
            new_color[assign_idx][0] += r
            new_color[assign_idx][1] += g
            new_color[assign_idx][2] += b
        for i in range(k):
            new_color[i][0] //= num[i]
            new_color[i][1] //= num[i]
            new_color[i][2] //= num[i]
        # 中心点の割当
        for i in range(k):
            min_dist = float("int")
            min_idx = 0
            color = None
            rc, gc, bc = new_color[i]
            for time in range(pixnum):
                column = time % len_col
                row = time // len_col
                r, g, b = image[row][column]
                dist = abs(r - rc) + abs(g - gc) + abs(b - bc)
                if dist <= min_dist:
                    min_idx = time
                    color = image[row][column]
            colors[i] = color
        # Cluster分類
        for time in range(pixnum):
            column = time % len_col
            row = time // len_col
            r, g, b = image[row][column]
            min_dist = float("inf")
            min_idx = 0
            for i in range(k):
                rc, gc, bc = colors[k]
                dist = abs(r - rc) + abs(g - gc) + abs(b - bc)
                if dist <= min_dist:
                    min_dist = dist
                    min_idx = i
            assign[time] = min_idx
            num[min_idx] += 1
    for i in range(k):
        print(i, colors)  # 出力
