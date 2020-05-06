def q1():
    import re
    with open("program.txt") as f1:
        txt = f1.read()
        len(re.findall(";", txt))


def q2():
    with open("program.txt") as f1:
        txt = f1.readlines()
        for i, line in enumerate(txt):
            if line in "main":
                print(i, line)


def q3():
    with open("program.txt") as f1:
        txt = f1.readlines()
        i = 0
        while i < len(txt):
            line = txt[i].rstrip()
            i += 1
            while i < len(txt) and line == txt[i].rstrip():
                i += 1
            print(line)


def q4():
    from bisect import bisect_left
    import hashlib
    # ハッシュ関数
    once = []
    twice = []
    with open("program.txt") as f1:
        txt = f1.readlines()
        i = 0
        count = 0
        while i < len(txt):
            m = hashlib.md5()
            line = txt[i].escape("unicode-escape")
            x = int(m.update(line).hexdigest(), 16)
            i = bisect_left(once, x)
            if i != len(once) and once[i] == x:
                # 1回表示されている
                j = bisect_left(twice, x)
                if j != len(once) and once[j] == x:
                    # すでに2回以上表示されている
                    pass
                else:
                    # 1回のみ
                    print(line)
                    twice.insert(j, x)
                    count += 1
            else:
                # 1回も表示されていない
                once.insert(i, x)
            i += 1
        print(count)


def q5():
    def similar(t0, t1):
        diff = 0
        for k in range(len(t1)):
            if k < len(t0):
                if t0[k] != t1[k]:
                    diff += 1
            else:
                if t1[k] != " ":
                    diff += 1
            if diff >= 5:
                return False
        if 1 <= diff < 5:
            return True
        else:
            return False

    with open("program.txt") as f1:
        txt = f1.readlines()
        idx = []
        for i in range(len(txt)):
            txt[i] = txt[i].rstrip()
            if len(txt[i]) >= 20:
                idx.append(i)
        i = 0
        j = 1
        for i in range(len(idx)):
            for j in range(i + 1, len(idx)):
                i0 = idx[i]
                i1 = idx[j]
                if len(txt[i0]) > len(txt[i1]):
                    i0, i1 = i1, i0
                # 常にtxt[i0]のほうが短い
                t0 = txt[i0]
                t1 = txt[i1]
                if similar(t0, t1):
                    print(t0)
                    print(t1)
                    print("")


def q7():
    with open("program.txt") as f1:
        txt = f1.readlines()
        i = 0
        while i < len(txt):
            line = txt[i].rstrip()
            i += 1
            count = 1
            while i < len(txt) and line == txt[i].rstrip():
                i += 1
                count += 1
            if count >= 4:
                print(line)


def levenshtein_distance(first_word, second_word):
    # The longer word should come first
    if len(first_word) < len(second_word):
        return levenshtein_distance(second_word, first_word)

    if len(second_word) == 0:
        return len(first_word)

    previous_row = range(len(second_word) + 1)

    for i, c1 in enumerate(first_word):

        current_row = [i + 1]

        for j, c2 in enumerate(second_word):

            # Calculate insertions, deletions and substitutions
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)

            # Get the minimum to append to the current row
            current_row.append(min(insertions, deletions, substitutions))

        # Store the previous row
        previous_row = current_row

    # Returns the last element (distance)
    return previous_row[-1]


def q6():
    with open("program.txt") as f1:
        txt = f1.readlines()
        idx = []
        for i in range(len(txt)):
            txt[i] = txt[i].rstrip()
            if len(txt[i]) >= 20:
                idx.append(i)
        i = 0
        j = 1
        for i in range(len(idx)):
            for j in range(i + 1, len(idx)):
                i0 = idx[i]
                i1 = idx[j]
                t0 = txt[i0]
                t1 = txt[i1]
                if levenshtein_distance(t0, t1) < 4:
                    print(t0)
                    print(t1)
                    print("")
