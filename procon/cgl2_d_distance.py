from geometric import Segment, Point
q = int(input())

for _ in range(q):
    x0, y0, x1, y1, x2, y2, x3, y3 = map(int, input().split())
    s1 = Segment(Point(x0, y0), Point(x1, y1))
    s2 = Segment(Point(x2, y2), Point(x3, y3))
    print(s1.getDistance(s2))
