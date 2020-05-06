import numbers
from math import isclose
from math import sqrt, cos, sin, tan, acos, asin, atan, atan2
from typing import List

eps = 0.0000001


class Point():
    def __init__(self, x=0, y=0, z=0) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other: "Point") -> "Point":
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: "Point") -> "Point":
        return Point(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other: ["Point", numbers.Number]) -> "Point":
        if isinstance(other, numbers.Number):
            return Point(self.x * other, self.y * other, self.z * other)
        elif isinstance(other, Point):  # 点同士は外積をとる
            return Point(
                self.y * other.z - self.z * other.y,
                self.z * other.x - self.x * other.z,
                self.x * other.y - self.y * other.x)

    def cross(self, p: "Point") -> numbers.Number:  # 外積の大きさ
        return self.x * p.y - self.y * p.x

    def __matmul__(self, other: "Point") -> numbers.Number:  # 内積
        return self.x * other.x + self.y * other.y + self.z * other.z

    def dot(self, other: "Point") -> numbers.Number:
        return self @ other

    def norm(self) -> numbers.Number:
        return self.x * self.x + self.y * self.y + self.z * self.z

    def abs(self) -> numbers.Number:
        return (self.x * self.x + self.y * self.y + self.z * self.z)**0.5

    def __lt__(self, other: "Point") -> bool:
        if self.x != other.x:
            return self.x < other.x
        elif self.x != other.y:
            return self.y < other.y
        else:
            return self.z < other.z

    def __eq__(self, other: "Point") -> bool:
        return isclose(self.x, other.x)and isclose(self.y, other.y) and isclose(self.z, other.z)

    def isOrthogonal(self, other: "Point") -> bool:
        return isclose(self @ other, 0)

    def isParallel(self, other: "Point") -> bool:
        if isinstance(other, Point):
            return (self * other).abs()

    def getDistance(self, b: "Point") -> numbers.Number:
        return (self - b).abs()

    def arg(self) -> numbers.Number:
        return atan2(self.x, self.y)

    def polar(self, a: numbers.Number, r: numbers.Number) -> "Point":
        self.x = cos(r) * a
        self.y = sin(r) * a
        return self


class Segment():
    def __init__(self, p1: "Point", p2: "Point") -> None:
        self.p1 = p1
        self.p2 = p2

    def isOrthogonal(self, other: "Segment") -> bool:  # other: segment
        return isclose((self.p2 - self.p1) @ (other.p2 - other.p1), 0)

    def isParallel(self, other: "Segment") -> bool:
        return isclose(((self.p2 - self.p1) * (other.p2 - other.p1)).abs(), 0)

    def project(self, p: "Point") -> "Point":
        base = self.p2 - self.p1
        r = ((p - self.p1)@base) / base.norm()
        return self.p1 + base * r

    def reflect(self, p: "Point") -> "Point":
        return p + (self.project(p) - p) * 2

    def getDistanceLP(self, p: "Point") -> numbers.Number:  # cross(*)は外積、segment を　lineとしてみた場合
        return ((self.p2 - self.p1) * (p - self.p1)).abs() / (self.p2 - self.p1).abs()

    def getDistanceSP(self, p: "Point") -> numbers.Number:
        if (self.p2 - self.p1) @ (p - self.p1) < 0:
            return (p - self.p1).abs()
        if (self.p1 - self.p2) @ (p - self.p2) < 0:
            return (p - self.p2).abs()
        return self.getDistanceLP(p)

    def getDistance(self, s2: "Segment") -> numbers.Number:  # s2:segment
        if (self.intersect(s2)):
            return 0
        return min(min(self.getDistanceSP(s2.p1), self.getDistanceSP(s2.p2)),
                   min(s2.getDistanceSP(self.p1), s2.getDistanceSP(self.p2)))

    def intersect(self, s2: "Segment") -> bool:  # s2:segment
        return intersect(self.p1, self.p2, s2.p1, s2.p2)

    def getCrossPoint(self, s2: "Segment") -> "Point":  # 交点
        base = s2.p2 - self.p1
        d1 = (base * (self.p1 - s2.p1)).abs()
        d2 = (base * (self.p2 - s2.p1)).abs()
        t = d1 / (d1 + d2)
        return self.p1 + (self.p2 - self.p1) * t


class Circle():
    def __init__(self, c: "Point", r: numbers.Number) -> None:
        self.c = c
        self.r = r

    def getCrossPoints(self, l: ["Segment", "Circle"]) -> List["Point"]:
        if isinstance(l, Segment):
            pr = l.project(self.c)
            e = (l.p2 - l.p1) / (l.p2 - l.p1).abs()
            base = sqrt(self.r * self.r - (pr - self.c).abs())
            return (pr + e * base, pr - e * base)
        elif isinstance(l, Circle):
            c2 = l
            d = (self.c - c2.c).abs()
            a = acos((self.r * self.r + d * d - c2.r * c2.r)) / (2 * self.r * d)
            t = (c2.c - self.c).arg()
            return (self.c + Point().polar(self.r, t + a), self.c + Point().polar(self.r, t - a))


def ccw(p0: "Point", p1: "Point", p2: "Point") -> int:
    a = p1 - p0
    b = p2 - p0
    if a.cross(b) > eps:
        return 1  # counter_clockwise
    if a.cross(b) < -eps:
        return -1  # clockwise
    if a@b < -eps:
        return 2  # online_back
    if a.norm() < b.norm():
        return -2  # online_front


def intersect(p1: "Point", p2: "Point", p3: "Point", p4: "Point") -> bool:
    return (ccw(p1, p2, p3) * ccw(p1, p2, p4) <= 0 and ccw(p3, p4, p1) * ccw(p3, p4, p2) <= 0)

# polygon vector
