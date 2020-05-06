m = 1000000
nil = -1
table = [nil] * m

# ハッシュ法だが、pythonではえらーになる


def h1(key):
    return key % m


def h2(key):
    return 1 + key % (m - 1)


def hash(key, i):
    return (h1(key) + i * h2(key)) % m


def insert(key):
    i = 0
    while True:
        hashed_key = hash(key, i)
        if table[hashed_key] == nil:
            table[hashed_key] = key
            return hashed_key
        else:
            i += 1


def search(key):
    i = 0
    while True:
        hashed_key = hash(key, i)
        if table[hashed_key] == key:
            return hashed_key
        elif table[hashed_key] == nil or i >= m:
            return nil
        else:
            i += 1


def str2key(key_str):
    key = 0
    count = 0
    for char in key_str:
        if char == "A":
            num = 1
        elif char == "C":
            num = 2
        elif char == "G":
            num = 3
        elif char == "T":
            num = 4
        key += num * (5**count)
        count += 1
    return key


def main():
    n = int(input())
    result_str = ""
    for _ in range(n):
        command, key_str = input().split(" ")
        key = str2key(key_str)
        if command == "insert":
            insert(key)
        elif command == "find":
            res = search(key)
            if res > -1:
                result_str += "yes\n"
            else:
                result_str += "no\n"
    print(result_str, end="")


if __name__ == "__main__":
    main()
