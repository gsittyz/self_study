def main():
    from geometric import Segment, Point
    x1, y1, x2, y2 = map(int, input().split())
    line = Segment(Point(x1, y1), Point(x2, y2))
    q = int(input())
    for _ in range(q):
        x0, y0 = map(int, input().split())
        p = line.reflect(Point(x0, y0))
        print(p.x, p.y)


if __name__ == "__main__":
    main()
