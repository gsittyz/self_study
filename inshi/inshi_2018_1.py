# (1)(2)
with open("./inshi/image1.txt") as f1:
    lines = f1.readlines()
    len_row = len(lines)
    len_column = len(lines[0].rstrip().split()) // 3
    pixnum = len_row * len_column
    print(pixnum)
    print(len_column)
