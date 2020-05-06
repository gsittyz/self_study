from geometric import Segment, Point


def main():
    q = int(input())
    for _ in range(q):
        x0, y0, x1, y1, x2, y2, x3, y3 = map(int, input().split())
        s1 = Segment(Point(x0, y0), Point(x1, y1))
        s2 = Segment(Point(x2, y2), Point(x3, y3))
        if s1.isOrthogonal(s2):
            print(2)
        elif s1.isParallel(s2):
            print(1)
        else:
            print(0)


if __name__ == "__main__":
    main()
